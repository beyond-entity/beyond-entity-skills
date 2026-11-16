# Tool schemas, output contracts and guide delivery

## Choose the current contract

Call `beyond_get_mcp_version` when checking compatibility. `beyond_get_definitions()` provides an index; request actual tool names or schema/guide IDs through `definition_names`. `mode="input_schema"` returns compact tool input/output schemas; `mode="full"` returns complete matching definitions. Read only the relevant tool/guide.

Offline source-derived contracts are in [tools.md](tools.md). Each tool JSON includes its description/help, inputSchema, declared outputSchema, and transitive local definitions needed by `$ref`. `outputSchema: null` explicitly means the source does not declare an output schema; it does not mean no output. Read live help/results and handlers when needed rather than inventing an output contract. General workflows below supplement, but do not replace, each tool's schema.

These are source baseline contracts from the dynamic public-definition loader, including generated type policies. They do not prove deployed remote or desktop wrapper schemas match. Prefer connected tool definitions and returned data; report unsupported version differences. Required properties, enum types, null/omission behavior and tool-specific side effects matter. Do not add proposed capability/help/read-token parameters.

## Inputs and saved outputs

- Use returned IDs, not examples or placeholders. Read target objects immediately before changes when relevant state could have changed.
- Entity create items nest `entity_info`; processor items nest `processor_info` with port attribute arrays. Read their exact schemas instead of sending read-result objects back as create payloads.
- Omitted fields often preserve current values, while null may clear or be rejected; consult each property. Endpoint lists replace their collection. Preserve existing IDs on retained contracts.
- Read returned auto-created attributes/constraints/contracts and generated IDs. Do not create duplicates or infer IDs from names.
- Some tools are atomic per item, some for the whole request. Inspect `created_*`, `failed`, operation receipts and current tool semantics before retrying.
- Development compact receipts may disclose server-generated defaults/IDs without returning a whole saved record. Fetch full records only when needed to verify content.

## JSON transport paging

Large responses, including failed/partially successful writes, may be paged. Inspect `data.operation_status.success`, `is_error`, `failed_count`, `failed_preview` immediately. Outer `success=true` can mean only that a page was delivered. `failed_preview` is bounded, not the full list.

Follow `paging.result_id` / `paging.next_cursor` with `beyond_get_result_page`. Collect `page_content` from every page, including the initial page, in order; concatenate fragments and parse the assembled JSON once. Individual fragments need not be valid JSON. Inspect the full final operation outcome, saved IDs and failed entries before retrying only failures.

An expired result cache is not permission to replay a write. Re-read affected objects to recover current state. In particular, do not retry model creation to recover guide pages. Transport paging is distinct from [lineage graph continuations](lineage.md) and ordinary limit/offset list pagination.

Use `include_json_content=false` when supported and structured content is available to avoid duplicate text JSON. Do not force all responses inline just to avoid handling pages.

## Guide revisions and context loss

`guide_id`, `guide_revision`, `delivery` and `details` identify an applicable guide. First delivery or a changed revision includes full content; repeated responses can be references. Read the content and follow the rules; a remembered guide ID alone is insufficient. Re-fetch via the provided `details` call with `mode="full"`, `include_examples=true` after context loss. Paged delivery is recorded only after all pages are returned.

Planning responses use inline current/next guidance; read it directly. Next steps are conditional and do not grant task authorization. A standalone guide read is optional there.

The inspected code tracks delivery, not whether an AI read or understood the Skill. It does not establish the previously proposed acknowledgement-token gate. Installing this package changes neither server enforcement nor runtime tool availability.
