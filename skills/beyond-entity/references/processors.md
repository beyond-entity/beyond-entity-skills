# Processor IO and HTTP contracts

## Choose and read the type

A processor is a modeled unit of work; a module-capable type can group multiple operations. Read current model `acceptable_processors`, then `processor_design_guide:<selected_type>`. The global catalog is not permission to create every type in a given model.

`beyond_create_processors` / `beyond_create_model_objects` use `processor_info` plus `input_attributes`, `output_attributes` and, only where allowed, `lookup_attributes`. `processor_info` requires logical `processor_name`, physical `module_name` and `processor_storage_type`. Use exact [tool schemas](tools.md) for optional metadata.

## IO semantics

- `INPUT`: externally supplied values available before processing. Do not project these outward as another processor's result.
- `OUTPUT`: verified final externally exposed results.
- `LOOKUP`: internal fetched, derived or temporary values when the selected type allows them. Add only when a transformation needs them.
- `NONE`: ordinary entity/data attributes, not processor ports; not subject to processor IO restrictions.

Inside a processor, INPUT→LOOKUP, INPUT→OUTPUT, LOOKUP→LOOKUP and LOOKUP→OUTPUT are valid. Do not write back to INPUT. From an external processor, project OUTPUT (or unrestricted NONE), not its INPUT/LOOKUP. Predicates may bind verified source INPUT/LOOKUP as request context; that does not turn them into readable response projections.

`use_lookup` is catalog policy, not a per-instance override. When false, new LOOKUP attributes are rejected and automatic SQL targets use OUTPUT. Existing legacy LOOKUP data is retained, not silently migrated. `use_lookup=true` permits intermediate values but does not require an artificial extra step. Neither setting means transformations are optional for real data flows.

## Routes and nested handler contracts

Read live `controller_endpoint_contract_guide`, `http_metadata_guide`, `endpoint_cardinality_guide` and, when needed, `external_api_design_guide` / `api_server_naming_contract`.

Use `endpoints` as an array of verified path/method/handler objects. Only catalog `is_module=true` allows multiple endpoints; other types allow at most one. The client cannot override the flag. An API Server processor represents one OpenAPI operation. Logical API name and physical function/class identifier are separate.

For applicable controller/handler types, a verified handler gets one INPUT and one OUTPUT OBJECT container. Same-handler routes share a pair. Unknown handlers do not create a fabricated contract; empty containers do not assert an HTTP body shape. Add only verified children beneath returned contract IDs using catalog physical types and HTTP parameter flags.

Re-read endpoints and attributes before an edit. Preserve `endpoint_id`, `input_attribute_id`, `output_attribute_id` for retained routes; omit old IDs for genuinely new/split routes. Updates replace the array: omission preserves, a list replaces, `[]` removes routes, `null` clears routing. Removed routes do not automatically delete old contracts, fields or lineage. Review cleanup explicitly.

Use `alias.OUTPUT.handler.field` for source response children and `AS "handler.field"` for an existing target response child. Caller INPUT binds support `:handler.field` / `:INPUT.handler.field`. Pre-create verified nested response fields; do not invent top-level OUTPUT fields merely to make SQL conversion succeed. Preserve nested physical/logical data types, including Rust generic metadata where applicable.

After creation/modification, inspect auto-created contract attributes and IDs rather than creating duplicates. Verify routes, IO, mappings and allowed types through a fresh processor read with `include_transformations=true`.

Full selected baseline guides are available from [the guide index](guides.md); use live selected-type guides for technology-specific behavior.
