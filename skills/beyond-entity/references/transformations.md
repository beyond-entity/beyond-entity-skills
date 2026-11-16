# Transformations and SQL data-flow notation

Read current `transformation_design_guide` and, for handler bindings, `controller_sql_input_guide`. Read source/target objects, attributes and existing transformations before editing. Use `beyond_get_processor(include_transformations=true)` / `beyond_get_transformations`.

## Represent actual flows

BE SQL is data-flow notation; BE records lineage and does not execute the SQL. Review verified flows across UI/state, controller, service, integration and storage layers, including code that never runs SQL. One processor may contain multiple transformations.

Use `beyond_add_transformation_by_sql` with `processor_id` and a supported single SELECT, INSERT, UPDATE or DELETE. A SELECT maps verified source results or caller inputs to the current processor. INSERT into another processor maps arguments directly to its existing INPUT; it does not assert a runtime database write. Preserve verified expressions and conditions.

Read all `auto_created_attributes` and IDs. Do not add them twice. Automatic targets are flat and follow `use_lookup`; pre-create nested targets when object/array contracts matter. Reuse verified OUTPUT targets for final results. Never create dummy INPUT, OUTPUT, LOOKUP, payload entities or `SELECT 1` just to draw an edge.

## Identify objects and fields precisely

Use verified physical names with aliases and explicit result aliases. Quote punctuation, spaces and literal dots with double quotes/backticks; escape an embedded quote by doubling it. A quoted `"model.onnx"` is one name; unquoted `schema.table` is qualified. Single quotes are strings.

If names collide, qualify with a verified model ID/name/schema, or use `BE_OBJECT('<verified object ID>')`. A bare ID-shaped identifier is still interpreted as a name. Cross-model sources are permitted within current canvas permissions. Never pick an ambiguous candidate without checking it.

Keep external/request values as named binds such as `:customerId`; do not inline real user values. External processor SELECT projections read OUTPUT/NONE, while predicates can bind request INPUT/LOOKUP. For controllers, use exact handler paths and current nested contracts. INSERT destinations must resolve to existing callee INPUT fields; do not fall back to similarly named OUTPUT/LOOKUP. Mixed controller handlers are rejected.

## Parser boundaries and recovery

Use `SQL_SYNTAX`, `SQL_OBJECT_NOT_FOUND`, `SQL_ATTRIBUTE_NOT_FOUND`, `SQL_AMBIGUOUS_OBJECT`, `SQL_AMBIGUOUS_ATTRIBUTE`, `SQL_ACCESS_DENIED` and `SQL_UNSUPPORTED` to choose a correction. Refresh live schemas/fields and correct SQL or verified model gaps. Do not rename objects or invent schema to suppress errors. A failed single conversion must not be treated as saved work.

The baseline supports top-level SELECT UNION / UNION ALL / UNION DISTINCT with positional targets named by the first SELECT. Branch predicates stay separate. INTERSECT/EXCEPT, nested/parenthesized compound queries, aggregate/GROUP BY branches, INSERT with compound SELECT and compound ordering/limits are outside that contract. Read the exact [tool description and schemas](tools/beyond_add_transformation_by_sql.json) before using advanced syntax; the live server may differ.

Parameterless SQL reads may create object-level QUERY_PARAMETER dependencies without attribute IDs. This does not provide a general execution-call graph. For pure control calls, DDL or unsupported propagation, record caller, target, condition and actual source evidence in supported metadata/documents; state the representation gap. In-memory results do not imply a backing store.

Re-read saved transformation IDs, target attributes, conditions and ordering. Existing transformations are not implicitly rewritten/deleted, and stored raw SQL is not rewritten on renames. Before completion, inspect `transformation_check` / warnings and report saved/reused mappings, justified exclusions and unresolved flows. A successful conversion proves only that submitted mapping.
