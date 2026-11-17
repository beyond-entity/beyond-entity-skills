# Beyond Entity Skills

**English** · [한국어](README_ko.md)

This repository contains a draft Skill for AI clients using Beyond Entity MCP. The Skill source is in `skills/beyond-entity/`. Shared rules live in `SKILL.md`, workflow guidance in `references/`, and tool input/output schemas and help in individual JSON files. Read only the files relevant to the current task.

The reference baseline comes from the actual public definition loader and guide/help implementations in `beserv`, at source MCP version **3.2.53**. This baseline does not establish compatibility with a deployed server. See [source provenance](skills/beyond-entity/references/source-provenance.json) for source hashes. Tools without a declared `outputSchema` have a null output schema, so missing output contracts are explicit.

## Transformation names

The Skill covers `beyond_rename_transformation` for changing an existing transformation's display name while preserving its ID, original SQL, processing order, items, and lineage. Read the current transformations first, use a short action-and-purpose name, and verify the saved result. See [transformation guidance](skills/beyond-entity/references/transformations.md).

## Installation

Copy or link the entire `skills/beyond-entity` folder into your AI client's supported Skill location. Copying only `SKILL.md` omits the references. A Codex user Skill location is `~/.agents/skills/beyond-entity`. Check for an existing Skill with the same name before installing. Consult other clients' documentation for their installation paths and reload behavior.

The app and AI clients use the same release ZIP for direct GitHub downloads. If release assets have not been published, the packaging command below can build a local ZIP. Automatic installation, login refresh, and server-enforced reading are currently unimplemented. Installing the local Skill does not establish an MCP connection or acknowledge server guide delivery.

## Refresh references and validate

Regenerate tool contracts from a trusted local `beserv` checkout using a Python environment with its dependencies installed. The exporter executes the checkout's Python definition builders.

```sh
/path/to/beserv/.venv-mcp-build/bin/python scripts/export_reference.py --source /path/to/beserv
python3 scripts/validate.py
python3 scripts/build_package.py --output /path/to/package-output
```

The exporter reads server source without modifying it or accessing project data. It regenerates the tool contracts and selected help snapshots used as the initial migration baseline. Workflow Markdown is maintained in this repository. A future single-source guide integration will require the server to consume a pinned content version from this repository. Existing server Skill and guide sources are still in place.

Validation checks Skill links, JSON references, input/output schema availability, tool and guide counts, and file hashes. It does not exercise live MCP operations or project writes. The package contains the complete installable Skill and its manifest. An external SHA-256 receipt accompanies the ZIP for integrity verification. The receipt does not authenticate the publisher, and packaging alone does not establish runtime compatibility.
