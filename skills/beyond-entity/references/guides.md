# Selected guide index

Read only the applicable guide. These are baseline source-generated bodies, not a promise that a connected remote runtime has the same revision. For live content, use `beyond_get_definitions(definition_names=[guide_id], mode="full", include_examples=true)`. Type-specific manuals stay on demand: request `model_design_guide:<type>`, `entity_design_guide:<type>` or `processor_design_guide:<type>` from the active runtime.

| Guide | Read when |
| --- | --- |
| [design_navigation_guide](guides/design_navigation_guide.json) | Discover current technologies before selecting a model. |
| [model_selection_guide](guides/model_selection_guide.json) | Compare model boundaries when the technology choice is unclear. |
| [transformation_design_guide](guides/transformation_design_guide.json) | Design actual data movement across UI, service and storage layers. |
| [processor_io_guide](guides/processor_io_guide.json) | Interpret general IO; selected-type policy remains authoritative. |
| [query_dependency_guide](guides/query_dependency_guide.json) | Represent verified parameterless reads and document pure-call gaps. |
| [controller_endpoint_contract_guide](guides/controller_endpoint_contract_guide.json) | Create/preserve handler-level nested request/response contracts. |
| [controller_sql_input_guide](guides/controller_sql_input_guide.json) | Resolve controller INPUT binds and mixed storage INSERT mappings. |
| [http_metadata_guide](guides/http_metadata_guide.json) | Use HTTP metadata and parameter flags. |
| [endpoint_cardinality_guide](guides/endpoint_cardinality_guide.json) | Check module versus single-operation endpoint limits. |
| [api_server_naming_contract](guides/api_server_naming_contract.json) | Separate logical API names from physical identifiers. |
| [external_api_design_guide](guides/external_api_design_guide.json) | Model verified external API operations. |
| [messaging_design_guide](guides/messaging_design_guide.json) | Model messaging boundaries and verified configuration. |
| [sqlite_storage_boundary_guide](guides/sqlite_storage_boundary_guide.json) | Distinguish authoritative SQLite storage from caches. |
| [attribute_security_guide](guides/attribute_security_guide.json) | Set PII/encryption metadata with exact enum/null semantics. |
| [security_findings_guide](guides/security_findings_guide.json) | Write findings and scoped complete/partial scans. |
| [code_analysis_guide](guides/code_analysis_guide.json) | Track bounded AI/parser runs and coverage evidence. |
| [checkpoint_run_guide](guides/checkpoint_run_guide.json) | Interpret checkpoint windows and run handoffs. |
| [development_planning_guide](guides/development_planning_guide.json) | Manage requirements, scenarios, estimates and Markdown reports. |
