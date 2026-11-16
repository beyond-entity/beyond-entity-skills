#!/usr/bin/env python3
"""Validate portable links, self-contained schema refs and exported source receipts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "beyond-entity"
REF = SKILL / "references"


def local_refs(node: object):
    if isinstance(node, dict):
        if isinstance(node.get("$ref"), str):
            yield node["$ref"]
        for key, child in node.items():
            if key not in {"example", "examples", "default", "const", "enum"}:
                yield from local_refs(child)
    elif isinstance(node, list):
        for child in node:
            yield from local_refs(child)


def validate() -> dict:
    body = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert body.startswith("---\nname: beyond-entity\ndescription: "), "Invalid Skill frontmatter"
    assert "[TODO" not in body, "Unfinished Skill scaffold"
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for raw in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in raw or raw.startswith("#"):
                continue
            target = (path.parent / unquote(raw.split("#", 1)[0])).resolve()
            assert target.is_relative_to(ROOT), f"Nonportable link: {path}: {raw}"
            assert target.is_file(), f"Broken link: {path}: {raw}"

    provenance = json.loads((REF / "source-provenance.json").read_text())
    tools = list((REF / "tools").glob("*.json"))
    assert len(tools) == provenance["public_tool_count"], "Tool count differs"
    output_count = 0
    for path in tools:
        tool = json.loads(path.read_text())
        assert path.stem == tool["name"], f"Tool identity mismatch: {path}"
        assert tool["source_mcp_version"] == provenance["source_mcp_version"]
        assert isinstance(tool["inputSchema"], dict), f"Missing input schema: {path}"
        output_count += int(tool["output_schema_declared"])
        assert tool["output_schema_declared"] == (tool["outputSchema"] is not None)
        for field in ("inputSchema", "outputSchema"):
            schema = tool[field]
            if schema is None:
                assert tool.get("output_contract_note"), f"Unexplained output gap: {path}"
                continue
            for ref in local_refs(schema):
                assert ref.startswith("#/"), f"Non-local schema ref: {path}: {ref}"
                value = schema
                try:
                    for part in unquote(ref[2:]).split("/"):
                        part = part.replace("~1", "/").replace("~0", "~")
                        value = value[int(part)] if isinstance(value, list) else value[part]
                except (KeyError, IndexError, ValueError, TypeError) as exc:
                    raise AssertionError(f"Unresolved {field} ref: {path}: {ref}") from exc
    assert output_count == provenance["declared_output_schema_count"]
    guides = list((REF / "guides").glob("*.json"))
    assert len(guides) == provenance["selected_guide_count"]
    for path in guides:
        guide = json.loads(path.read_text())
        assert guide["guide_id"] == path.stem
        digest = hashlib.sha256(json.dumps(guide["content"], sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]
        assert digest == guide["guide_revision"], f"Guide revision mismatch: {path}"
    for relative, expected in provenance["generated_file_sha256"].items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f"Export drift: {relative}"
    return {"tools": len(tools), "declared_output_schemas": output_count,
            "undeclared_output_schemas": len(tools) - output_count,
            "guides": len(guides), "skill_lines": len(body.splitlines()),
            "source_mcp_version": provenance["source_mcp_version"]}


if __name__ == "__main__":
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
