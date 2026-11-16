# Models, entities and relationships

## Select a supported model

Read live `design_navigation_guide` through `beyond_get_definitions`, then only `model_design_guide:<selected_type>`. The global catalog is distinct from an existing model's `acceptable_entities` / `acceptable_processors`: the latter are creation allowlists for that model. For remote projects, active remote definitions take precedence over a local source snapshot.

Use the verified technology. For example, React architecture uses `react_application`; browser workflow models may use `webapp`, and application UI workflows may use `app`. Do not add Tauri unless requested or verified. Framework backends use their registered application model. Messaging uses the appropriate RabbitMQ/Kafka model. `general_system` is for applicable generic boundaries, not a substitute for checking a supported framework.

Read the model's returned storage guide and selected entity/processor type guide before creation. These contain storage-specific data types, naming, allowed types, default fields and IO policy. Only load the technology manuals required for the task. Do not copy all storage types into a new project.

## Names and evidence

Logical names (`model_name`, `entity_name`, `attribute_name`, `processor_name`) express business meaning in the user's language. Physical names (`database_name`, `table_name`, `column_name`, `module_name`) match verified code/storage conventions. Do not change physical names to accommodate a parser.

For code extraction, verify framework, class, route and subtype from source/configuration. Preserve class tracing metadata where appropriate (`package_name`, `qualified_class_name`, `source_file`); avoid guessing from naming alone. Read selected-type guides for class-versus-operation semantics.

## Create or update entities

`beyond_create_entities` accepts `model_id` and `entities`, where each item has `entity_info` and optional `attributes` / `constraints`. `entity_info` requires `entity_name`, `table_name`, `entity_storage_type`; attribute creation requires `attribute_name`, `column_name`, `data_type`. Read the [exact schema](tools/beyond_create_entities.json) before constructing optional fields.

Storage default fields may be auto-created; supplied root fields with matching physical names take precedence. Read returned `attributes`, `auto_created_attributes`, `auto_created_attribute_ids` and `auto_created_constraints`. Do not separately recreate default fields, PKs or defaults that the server already created. Existing entities and type changes are not automatically backfilled.

Hierarchy names in a creation batch resolve within their documented scope. Use verified parent IDs for later additions when supported; preserve nested object/array structure. Follow catalog data types, dimensions and nested-type metadata. For vector indexes use the selected catalog/constraint rules (for pgvector similarity: `cosine`, `l2`, `inner_product`). Attribute security has a [separate contract](security.md).

Each entity is atomic but a batch can partially succeed. Inspect the complete created/failed lists and retry only failures. Re-read saved objects and constraints before reporting completion.

## Relationships and deletion

Prefer explicit `parent_entity_id` / `parent_attribute_ids` and `child_entity_id` / `child_attribute_ids` after checking the [relationship tool schema](tools/beyond_create_relationships.json). Parent owns the complete PK; child owns the FK. Preserve pair ordering. Legacy `from` / `to` names have surprising direction and alias semantics; never infer their meaning from prefixes.

Choose optionality/identifying semantics explicitly using `relationship_type`; cardinality alone is insufficient. Check whether missing child columns will be auto-created and reuse existing verified columns when intended.

`on_delete` / `on_update` are reference metadata in `other_info`; BE does not execute or guarantee the referential actions. They can inform separately verified DDL/code generation.

Before deleting objects, attributes, constraints or models, read current dependents and the specific cascade contract. Apply only the requested deletion scope, inspect deletion receipts/failures, then re-read remaining objects. Do not silently recreate retained historical data or clean unrelated records.
