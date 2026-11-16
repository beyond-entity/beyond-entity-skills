#!/usr/bin/env python3
"""Build a deterministic whole-Skill ZIP and an external SHA-256 receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate import ROOT, SKILL, validate


def build(output: Path) -> Path:
    summary = validate()
    match = re.search(r'^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$',
                      (SKILL / "SKILL.md").read_text(), re.MULTILINE)
    if not match:
        raise SystemExit("Missing package version in Skill metadata")
    version = match.group(1)
    files = {}
    for path in sorted(SKILL.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Symlinks are not packaged: {path}")
        if path.is_file():
            files[path.relative_to(SKILL.parent).as_posix()] = path.read_bytes()
    manifest = {
        "schema_version": 1, "package_id": "beyond-entity", "version": version,
        "entrypoint": "beyond-entity/SKILL.md", "source_mcp_version": summary["source_mcp_version"],
        "compatibility": {"policy": "Connected tool definitions are authoritative; source baseline only.",
                          "validated_runtime_versions": []},
        "files": {name: {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
                  for name, data in files.items()},
    }
    files["beyond-entity/package-manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"beyond-entity-skill-{version}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as zip_file:
        for name, data in sorted(files.items()):
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zip_file.writestr(info, data)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / (archive.name + ".sha256")).write_text(f"{digest}  {archive.name}\n")
    print(json.dumps({"archive": str(archive), "sha256": digest, "packaged_files": len(files)}, indent=2))
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output.resolve())
