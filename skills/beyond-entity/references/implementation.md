# Code, analysis and implementation status

## Before editing code

Load current accessible entity/processor schemas through `beyond_load_schema`, including transformations, and keep them in working context. Identify affected processors by model, physical/logical names and verified source mappings. Use `beyond_get_processor(include_transformations=true)` and inspect connected inputs, outputs, storage attributes and transformations even for a bug fix or refactoring.

One file can implement several processors and one processor can span files. Preserve established contracts for behavior-preserving changes. When behavior changes, update affected BE objects, mappings and architecture documents within the authorized work, re-checking current BE state first. Do not create artificial architecture edits for a code-only refactoring.

If the processor/mapping cannot be found, report the gap and continue independent work. A connection error does not prove no design exists. Resolve contract ambiguity before dependent edits. Treat existing code/design divergence as evidence to investigate, not automatic permission to endorse either side.

## Code extraction and analysis runs

Read `code_analysis_guide` for code extraction/validation. Use `beyond_start_code_analysis` with a distinct run ID, actual existing targets, analyzer identity, source basis, explicit scope and limits. `source_commit` is from the source repository, not the BE model repository. AI work uses its own AI/HYBRID run.

Save authorized architecture work, then finish the analysis with actual observed results through `beyond_finish_code_analysis`. A run is bounded to 200 nodes; keep summaries within the returned limits and use `report_ref` for detail. Unsupported or unresolved paths are PARTIAL. Zero findings does not mean safe or CHECKED; CHECKED requires applicable rule IDs, completed checks and no unresolved boundary.

Retries must retain identical inputs for the same run ID. Changed payloads or stale revisions require re-reading and a new run, not overwriting newer observations. Run records are latest observations with bounded history, not historical node snapshots. They are excluded from BE Git staging/restore; an architecture diff does not reconstruct past security/analysis coverage.

## Status and verification

Use the live implementation/test enums from [the tool schemas](tools.md); do not invent values such as `done`. Coding, UX implementation and module test statuses are separate fields. Mark only the status justified by actual design/code/testing evidence. An estimated or generated implementation is not automatically IMPLEMENTED or TEST_PASSED.

Advanced processor implementation/UX status updates and new checkpoints return advisory `transformation_check` / `warnings`. Inspect check status, scope, missing processor count, `has_more` and coverage notes. `UNAVAILABLE` is not clean. Saves remain permitted; warning absence does not prove all flows are modeled.

Verify behavior against the current transformation design with checks appropriate to the change. Re-read saved objects, mappings and status, then perform the [checkpoint handoff](checkpoints.md) for authorized changes. Report code verification separately from BE synchronization and list pending work if MCP writes fail.
