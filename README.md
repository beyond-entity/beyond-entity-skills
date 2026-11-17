# Beyond Entity Skills

**English** · [한국어](README_ko.md)

This repository contains a draft Skill for AI clients using Beyond Entity MCP. The Skill source is in `skills/beyond-entity/`. Shared rules live in `SKILL.md`, workflow guidance in `references/`, and tool input/output schemas and help in individual JSON files. Read only the files relevant to the current task.

The reference baseline comes from the actual public definition loader and guide/help implementations in `beserv`, at source MCP version **3.2.53**. This baseline does not establish compatibility with a deployed server. See [source provenance](skills/beyond-entity/references/source-provenance.json) for source hashes. Tools without a declared `outputSchema` have a null output schema, so missing output contracts are explicit.

## Transformation names

The Skill covers `beyond_rename_transformation` for changing an existing transformation's display name while preserving its ID, original SQL, processing order, items, and lineage. Read the current transformations first, use a short action-and-purpose name, and verify the saved result. See [transformation guidance](skills/beyond-entity/references/transformations.md).

## Installation

Use an official stable asset from [Releases](https://github.com/beyond-entity/beyond-entity-skills/releases). Download `beyond-entity-skill-<version>.zip` and its matching `.zip.sha256` file. Verify the archive SHA-256, embedded package manifest, and file receipts before extracting.

Call `beyond_get_mcp_version` on the intended MCP connection. The package manifest's `compatibility.validated_runtime_versions` must include that exact version. The source baseline alone does not establish compatibility.

Install the entire `beyond-entity` folder into your AI client's supported Skill location. Copying only `SKILL.md` omits the references. A Codex user Skill location is `~/.agents/skills/beyond-entity`; a Claude Code personal Skill location is `~/.claude/skills/beyond-entity`. Preserve an existing installation and user changes, and avoid duplicate installations. Reload the client or start a new session when required for Skill discovery.

For a source checkout, the installable folder is `skills/beyond-entity/`. Locally built packages without a tested runtime list are suitable for inspection. Activate a package only after verifying its runtime compatibility.

Installing the Skill does not establish an MCP connection or acknowledge server guide delivery.

## Refresh references and validate

Regenerate tool contracts from a trusted local `beserv` checkout using a Python environment with its dependencies installed. The exporter executes the checkout's Python definition builders.

```sh
/path/to/beserv/.venv-mcp-build/bin/python scripts/export_reference.py --source /path/to/beserv
python3 scripts/validate.py
python3 scripts/build_package.py --output /path/to/package-output
```

The exporter reads server source without modifying it or accessing project data. It regenerates the tool contracts and selected help snapshots used as the initial migration baseline. Workflow Markdown is maintained in this repository. A future single-source guide integration will require the server to consume a pinned content version from this repository. Existing server Skill and guide sources are still in place.

Validation checks Skill links, JSON references, input/output schema availability, tool and guide counts, and file hashes. It does not exercise live MCP operations or project writes. The package contains the complete installable Skill and its manifest. An external SHA-256 receipt accompanies the ZIP for integrity verification. The receipt does not authenticate the publisher, and packaging alone does not establish runtime compatibility.

For a release candidate that has passed runtime verification, record the exact tested version when packaging:

```sh
python3 scripts/build_package.py --output /path/to/package-output --validated-runtime-version 3.2.53
```

The flag records verification performed by the maintainer. It does not run runtime tests or infer support from `source_mcp_version`. Omitting the flag leaves the validated runtime list empty.
