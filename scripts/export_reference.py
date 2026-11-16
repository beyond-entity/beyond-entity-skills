#!/usr/bin/env python3
"""Export an inspected beserv source baseline; never connect to project databases."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "skills" / "beyond-entity" / "references"
GUIDES = {
    "design_navigation_guide": "Discover current technologies before selecting a model.",
    "model_selection_guide": "Compare model boundaries when the technology choice is unclear.",
    "transformation_design_guide": "Design actual data movement across UI, service and storage layers.",
    "processor_io_guide": "Interpret general IO; selected-type policy remains authoritative.",
    "query_dependency_guide": "Represent verified parameterless reads and document pure-call gaps.",
    "controller_endpoint_contract_guide": "Create/preserve handler-level nested request/response contracts.",
    "controller_sql_input_guide": "Resolve controller INPUT binds and mixed storage INSERT mappings.",
    "http_metadata_guide": "Use HTTP metadata and parameter flags.",
    "endpoint_cardinality_guide": "Check module versus single-operation endpoint limits.",
    "api_server_naming_contract": "Separate logical API names from physical identifiers.",
    "external_api_design_guide": "Model verified external API operations.",
    "messaging_design_guide": "Model messaging boundaries and verified configuration.",
    "sqlite_storage_boundary_guide": "Distinguish authoritative SQLite storage from caches.",
    "attribute_security_guide": "Set PII/encryption metadata with exact enum/null semantics.",
    "security_findings_guide": "Write findings and scoped complete/partial scans.",
    "code_analysis_guide": "Track bounded AI/parser runs and coverage evidence.",
    "checkpoint_run_guide": "Interpret checkpoint windows and run handoffs.",
    "development_planning_guide": "Manage requirements, scenarios, estimates and Markdown reports.",
}


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(source: Path, *args: str) -> str | None:
    result = subprocess.run(["git", "-C", str(source), *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def group(name: str) -> str:
    if any(part in name for part in ("development_", "requirement")):
        return "Development planning"
    if "mcp_review" in name:
        return "MCP review board"
    if "security" in name:
        return "Security findings"
    if "code_analysis" in name or "implementation_status" in name or "test_status" in name:
        return "Analysis and implementation status"
    if "checkpoint" in name or "architecture_diff" in name:
        return "Checkpoints"
    if "document" in name:
        return "Project documents"
    if "transformation" in name or "lineage" in name:
        return "Transformations and lineage"
    if any(part in name for part in ("git_", "branch", "commit", "changes")):
        return "BE Git"
    if any(part in name for part in ("create_", "modify_", "delete_", "add_", "set_canvas")) and "project" not in name:
        return "Model writes"
    return "Discovery and reads"


def export(source: Path) -> None:
    if not (source / "be_mcp_core" / "definitions.py").is_file():
        raise SystemExit("--source must point to a trusted beserv source checkout")
    # Capture hashes before importing the exact local definition builders.
    inputs = [source / name for name in (
        "mcp_definition.json", "model_creation_schema.json", "mcp_usage_guide.json",
        "mcp_usage_guide_full.json", "be_desktop/mcp_usage_guide.json",
        "be_mcp_core/definitions.py", "be_mcp_core/schema_materialization.py",
        "be_mcp_core/guide_delivery.py", "be_mcp_core/response_paging.py",
        "be_mcp_core/tool_registry.py", "be_mcp_core/development_tools.py",
        "be_mcp_core/version.py", "be_mcp_core/reader_contract.py",
        "be_desktop/mcp_server.py", "be_server/mcp/service.py",
        "docs/beyond_entity_mcp_usage_guide_en.md", "docs/beyond_entity_mcp_usage_guide_ko.md",
        "be_core/project_db/attribute_security.py", "be_core/project_db/pii.py",
    )]
    inputs += sorted((source / "be_mcp_core" / "handlers").glob("*.py"))
    before = {p.relative_to(source).as_posix(): sha(p) for p in inputs if p.is_file()}
    sys.path.insert(0, str(source))
    from be_mcp_core.definitions import load_public_definition_document
    from be_mcp_core.schema_materialization import materialize_input_schema
    from be_mcp_core.version import MCP_SERVER_VERSION

    document = load_public_definition_document()
    definitions = document["definitions"]
    tools = document["tools"]
    names = [tool["name"] for tool in tools]
    if len(names) != len(set(names)):
        raise SystemExit("Duplicate public tool names")
    if document["mcp_server"]["version"] != MCP_SERVER_VERSION:
        raise SystemExit("Source JSON and Python MCP versions disagree")
    for name in GUIDES:
        if name not in definitions:
            raise SystemExit(f"Missing guide: {name}")
    for path, digest in before.items():
        if sha(source / path) != digest:
            raise SystemExit(f"Source changed while exporting: {path}; rerun from a stable checkout")

    generated = []
    rows: dict[str, list[str]] = {}
    for tool in tools:
        pool = {**definitions, **tool.get("definitions", {})}
        declared = tool.get("outputSchema") is not None
        payload = {
            "name": tool["name"],
            "description": tool.get("description", ""),
            "source_mcp_version": MCP_SERVER_VERSION,
            "inputSchema": materialize_input_schema(tool.get("inputSchema"), pool),
            "outputSchema": materialize_input_schema(tool.get("outputSchema"), pool),
            "output_schema_declared": declared,
        }
        if not declared:
            payload["output_contract_note"] = (
                "No outputSchema is declared by the inspected public source definition. "
                "Consult live help and actual results; do not infer a missing output contract."
            )
        path = REF / "tools" / f"{tool['name']}.json"
        dump(path, payload)
        generated.append(path)
        required = ", ".join(f"`{key}`" for key in payload["inputSchema"].get("required", [])) or "—"
        output = "declared" if declared else "not declared"
        rows.setdefault(group(tool["name"]), []).append(
            f"| [{tool['name']}](tools/{tool['name']}.json) | {required} | {output} |"
        )
    tool_index = ["# Tool input/output and Help index", "",
                  f"Source baseline: MCP {MCP_SERVER_VERSION}; {len(tools)} tools. Read only the relevant tool JSON.", "",
                  "Each file contains the tool description/help, self-contained inputSchema and declared outputSchema. "
                  "Required columns below show top-level fields only; nested and conditional requirements remain in the schema. "
                  "A missing declared output is explicit, not an empty response. Prefer live definitions for the connected runtime.", ""]
    for title, values in rows.items():
        tool_index += [f"## {title}", "", "| Tool | Top-level required | Output schema |", "| --- | --- | --- |", *values, ""]
    (REF / "tools.md").write_text("\n".join(tool_index), encoding="utf-8")
    generated.append(REF / "tools.md")

    guide_index = ["# Selected guide index", "",
                   "Read only the applicable guide. These are baseline source-generated bodies, not a promise "
                   "that a connected remote runtime has the same revision. For live content, use "
                   "`beyond_get_definitions(definition_names=[guide_id], mode=\"full\", include_examples=true)`. "
                   "Type-specific manuals stay on demand: request `model_design_guide:<type>`, "
                   "`entity_design_guide:<type>` or `processor_design_guide:<type>` from the active runtime.", "",
                   "| Guide | Read when |", "| --- | --- |"]
    for name, purpose in GUIDES.items():
        path = REF / "guides" / f"{name}.json"
        body = definitions[name]
        revision = hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]
        dump(path, {"guide_id": name, "guide_revision": revision,
                    "source_mcp_version": MCP_SERVER_VERSION, "content": body})
        generated.append(path)
        guide_index.append(f"| [{name}](guides/{name}.json) | {purpose} |")
    (REF / "guides.md").write_text("\n".join(guide_index) + "\n", encoding="utf-8")
    generated.append(REF / "guides.md")

    # Remove only obsolete generated JSON contracts; never authored Markdown.
    expected = {p.resolve() for p in generated}
    for directory in (REF / "tools", REF / "guides"):
        for path in directory.glob("*.json"):
            if path.resolve() not in expected:
                path.unlink()
    status = git(source, "status", "--porcelain", "--untracked-files=no")
    provenance = {
        "schema_version": 1,
        "source_project": "beserv",
        "source_mcp_version": MCP_SERVER_VERSION,
        "source_git_commit": git(source, "rev-parse", "HEAD"),
        "source_tracked_worktree_dirty": bool(status) if status is not None else None,
        "basis": "Current working-tree files, dynamically loaded through be_mcp_core.definitions.load_public_definition_document; commit alone is not the full source identity.",
        "source_file_sha256": before,
        "public_tool_count": len(tools),
        "declared_output_schema_count": sum(t.get("outputSchema") is not None for t in tools),
        "selected_guide_count": len(GUIDES),
        "generated_file_sha256": {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted(generated)},
        "limitations": [
            "No live project data was accessed and no runtime compatibility was exercised.",
            "Technology-specific guides are intentionally fetched on demand from the active runtime.",
            "Source-generated guide/schema snapshots are an initial migration baseline, not the completed single-source server integration.",
            "Current guide delivery tracking is not proof of Skill reading or comprehension and is not the proposed read gate.",
        ],
    }
    dump(REF / "source-provenance.json", provenance)
    print(f"Exported {len(tools)} tools, {len(GUIDES)} guides; {provenance['declared_output_schema_count']} declared output schemas")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    export(parser.parse_args().source.resolve())
