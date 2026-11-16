# Checkpoints, collaboration and BE Git

## Recover before changing

Read recent checkpoints and current relevant objects on initial connection/resumption. Human/other-agent changes can occur without being fully summarized in a checkpoint. Inspect available change records and code; preserve unrelated changes and current locks. Review-only access does not require creating a checkpoint.

## Run windows

For authorized change/analysis runs, read live `checkpoint_run_guide` and current tool side effects:

1. Read the newest `cp_at` as the current change window; create one only if absent and required for that authorized run.
2. Perform the authorized work; when recording linked security scans use the current window ID as `checkpoint_id`.
3. Use `beyond_update_checkpoint(cp_at, cp_message)` to summarize this window, including unchanged/failed analysis runs where relevant. It updates only the message and preserves original actor metadata.
4. Use `beyond_add_checkpoint` to open the next window at run end; use the returned `data.checkpoint.cp_at`. Provide actual known model identity/version in `actor_name`; do not invent one.

The handoff should state intent/rationale, changed BE IDs and code references, saved/reused transformations, verification, scope exclusions, unresolved issues and next work. Claim a save only after the server confirms it.

Remote `beyond_add_checkpoint` also exports/commits the BE working tree, without push. Local-project checkpoints do not run Git. If the Git commit fails after the checkpoint is saved, retry `beyond_git_commit` instead of creating another checkpoint. Inspect transformation warnings before reporting completion. Avoid redundant commits; follow the connected runtime's semantics.

## Change history interpretation

Changes after a checkpoint belong to that checkpoint. `beyond_get_architecture_diff` covers `[from_cp_at, to_cp_at)`. Both endpoints must exist; equal endpoints yield no changes. `action` is insert/update/delete; `node_json` for deletion contains the deleted object's old data and is not a live object. Never infer deletion from empty payloads or restore an object because its deleted payload is nonempty.

Within a window, insert→update stays insert, insert→delete disappears, update→delete becomes delete and delete→reinsert of an existing object becomes update. Reverted updates may still appear. `history_available=false` is missing history, not no changes. Analysis latest-state rows are not reconstructed by architecture diffs.

## Repository operations and MCP issue reviews

BE model Git and application source Git are separate. Source provenance must use the source repository commit. Before branch changes inspect current state; never discard another worker's work. Use `beyond_get_changes`, comparison/history tools and runtime-supported Git tools within the requested scope. Desktop Git adapters may be disabled; do not bypass that by opening the project database. A commit does not imply push authorization.

MCP review-board tools are separate from requirement discussions. If reporting/replying/resolving MCP issues is authorized, search for an existing report, read it, submit reproducible evidence with versions and exact failure scope, and verify receipts. A suggestion in an error/guide does not independently authorize sending a report or message. Tool schemas: [index](tools.md).
