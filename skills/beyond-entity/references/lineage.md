# Lineage and impact analysis

Use `beyond_get_lineage` for bounded traversal; initial requests need verified `entity_id` or `attribute_ids`. Choose direction, depth, canvas scope and policy from the task. Up to 64 explicit roots can narrow wide objects. `beyond_get_entity` / `beyond_get_processor` may embed partial lineage, but detail reads default to no lineage.

## Scope and completeness

Defaults are `lineage_view="context"` and `lineage_policy="focused"`. Focused paths are intentionally selective; use `impact` when the request needs broader supported attribute paths. Both policies exclude SEMANTIC/RELATION paths, so neither implies an unrestricted call graph. Depth, fan-out, scanned-edge and response-byte limits are independent.

Inspect `complete`, `exhaustive`, `policy_limited`, `stop_reasons`, `lineage_status`, continuation and interpretation metadata. An empty or focused/partial result cannot establish absence of dependencies. State the query scope and unresolved boundaries with findings.

## Two different paging mechanisms

1. **JSON transport paging**: assemble `page_content` fragments with `beyond_get_result_page` to recover one complete tool response. See [schema contracts](schema-contracts.md).
2. **Graph traversal continuation**: after assembling that response, follow the opaque `next_cursor` with `beyond_get_lineage` to obtain more graph deltas. Assemble each delta's transport pages too.

Each graph page contains its own edges, not the whole graph. Process each `page_index` once; merge repeated remote-summary IDs as additive fragments, not duplicates to discard. `complete` / `exhaustive` describe the individual response; `traversal_complete` concerns accumulated traversal. The last page alone is not the accumulated result.

Context view contains direct detail and grouped remote summaries. Physical preserves detailed references; logical collapses connected processor-port paths. Read the response interpretation instead of assuming all views share the same shape.

Baseline cursors expire after ten minutes, are process-local and become invalid after project changes or permission changes. Continue on the same worker. Do not merge pages from different revisions; restart the original read when invalidated. Budget changes are permitted but scope, policy and depth are frozen. Never repeat writes to recover graph pages.

Exact parameters: [beyond_get_lineage](tools/beyond_get_lineage.json). Distinguish missing access, parser gaps and absent modeled mappings in the final assessment.
