# Tool input/output and Help index

Source baseline: MCP 3.2.51; 100 tools. Read only the relevant tool JSON.

Each file contains the tool description/help, self-contained inputSchema and declared outputSchema. Required columns below show top-level fields only; nested and conditional requirements remain in the schema. A missing declared output is explicit, not an empty response. Prefer live definitions for the connected runtime.

## Discovery and reads

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_get_mcp_version](tools/beyond_get_mcp_version.json) | — | not declared |
| [beyond_get_usage_guide](tools/beyond_get_usage_guide.json) | — | not declared |
| [beyond_get_definitions](tools/beyond_get_definitions.json) | — | not declared |
| [beyond_create_project](tools/beyond_create_project.json) | `project_name` | declared |
| [beyond_get_my_organizations](tools/beyond_get_my_organizations.json) | — | declared |
| [beyond_list_projects](tools/beyond_list_projects.json) | — | declared |
| [beyond_checkout_project](tools/beyond_checkout_project.json) | `project_id` | not declared |
| [beyond_get_context](tools/beyond_get_context.json) | — | not declared |
| [beyond_get_project_overview](tools/beyond_get_project_overview.json) | `project_id` | not declared |
| [beyond_get_result_page](tools/beyond_get_result_page.json) | `result_id` | not declared |
| [beyond_load_schema](tools/beyond_load_schema.json) | — | declared |
| [beyond_get_canvas](tools/beyond_get_canvas.json) | `canvas_id` | declared |
| [beyond_search](tools/beyond_search.json) | `query` | declared |
| [beyond_find_attributes](tools/beyond_find_attributes.json) | — | declared |
| [beyond_get_model](tools/beyond_get_model.json) | `model_id` | declared |
| [beyond_get_entity](tools/beyond_get_entity.json) | `entity_id` | declared |
| [beyond_get_processor](tools/beyond_get_processor.json) | `processor_id` | declared |

## MCP review board

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_mcp_review_search](tools/beyond_mcp_review_search.json) | — | not declared |
| [beyond_mcp_review_submit](tools/beyond_mcp_review_submit.json) | `tool_name`, `category`, `summary` | not declared |
| [beyond_mcp_review_get](tools/beyond_mcp_review_get.json) | `review_id` | not declared |
| [beyond_mcp_review_reply](tools/beyond_mcp_review_reply.json) | `review_id`, `message` | not declared |
| [beyond_mcp_review_resolve](tools/beyond_mcp_review_resolve.json) | `review_id`, `resolution_status` | not declared |

## BE Git

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_switch_branch](tools/beyond_switch_branch.json) | `branch_name` | not declared |
| [beyond_git_commit](tools/beyond_git_commit.json) | `message` | not declared |
| [beyond_git_pull](tools/beyond_git_pull.json) | — | not declared |
| [beyond_git_push](tools/beyond_git_push.json) | — | not declared |
| [beyond_get_changes](tools/beyond_get_changes.json) | — | not declared |
| [beyond_compare_branches](tools/beyond_compare_branches.json) | `base_branch` | not declared |
| [beyond_compare_commits](tools/beyond_compare_commits.json) | `base_commit` | not declared |
| [beyond_get_commit_history](tools/beyond_get_commit_history.json) | — | not declared |

## Analysis and implementation status

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_get_implementation_status](tools/beyond_get_implementation_status.json) | — | declared |
| [beyond_update_entity_implementation_status](tools/beyond_update_entity_implementation_status.json) | `entity_id`, `implementation_status` | declared |
| [beyond_update_implementation_status](tools/beyond_update_implementation_status.json) | `object_type`, `object_id` | declared |
| [beyond_update_processor_implementation_status](tools/beyond_update_processor_implementation_status.json) | `processor_id` | declared |
| [beyond_update_processor_test_status](tools/beyond_update_processor_test_status.json) | `processor_id` | declared |
| [beyond_start_code_analysis](tools/beyond_start_code_analysis.json) | `run_id`, `metadata` | not declared |
| [beyond_finish_code_analysis](tools/beyond_finish_code_analysis.json) | `run_id`, `execution_status` | not declared |
| [beyond_get_code_analysis](tools/beyond_get_code_analysis.json) | — | not declared |
| [beyond_prune_code_analysis](tools/beyond_prune_code_analysis.json) | `before` | not declared |

## Checkpoints

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_list_checkpoints](tools/beyond_list_checkpoints.json) | — | declared |
| [beyond_get_architecture_diff](tools/beyond_get_architecture_diff.json) | `from_cp_at`, `to_cp_at` | declared |
| [beyond_add_checkpoint](tools/beyond_add_checkpoint.json) | `cp_message`, `actor_name` | declared |
| [beyond_update_checkpoint](tools/beyond_update_checkpoint.json) | `cp_at`, `cp_message` | declared |

## Project documents

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_list_documents](tools/beyond_list_documents.json) | — | declared |
| [beyond_get_document](tools/beyond_get_document.json) | — | declared |
| [beyond_add_document](tools/beyond_add_document.json) | `file_name`, `doc_content`, `actor_name` | declared |
| [beyond_update_document](tools/beyond_update_document.json) | `doc_id`, `actor_name` | declared |

## Model writes

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_create_model](tools/beyond_create_model.json) | `model_name`, `model_storage_type` | declared |
| [beyond_create_model_objects](tools/beyond_create_model_objects.json) | `model_id` | declared |
| [beyond_create_entities](tools/beyond_create_entities.json) | `model_id`, `entities` | declared |
| [beyond_create_processors](tools/beyond_create_processors.json) | `model_id`, `processors` | declared |
| [beyond_add_entity_attributes](tools/beyond_add_entity_attributes.json) | `entity_id`, `attributes` | declared |
| [beyond_add_processor_attributes](tools/beyond_add_processor_attributes.json) | `processor_id` | declared |
| [beyond_add_constraints](tools/beyond_add_constraints.json) | `entity_id`, `constraints` | declared |
| [beyond_create_relationships](tools/beyond_create_relationships.json) | `model_id`, `relationships` | declared |
| [beyond_set_canvas_layout](tools/beyond_set_canvas_layout.json) | `canvas_id` | declared |
| [beyond_modify_model](tools/beyond_modify_model.json) | `model_id`, `updates` | declared |
| [beyond_modify_entity](tools/beyond_modify_entity.json) | `entity_id`, `updates` | declared |
| [beyond_modify_processor](tools/beyond_modify_processor.json) | `processor_id`, `updates` | declared |
| [beyond_modify_entity_attribute](tools/beyond_modify_entity_attribute.json) | `attribute_id`, `updates` | declared |
| [beyond_modify_processor_attributes](tools/beyond_modify_processor_attributes.json) | — | declared |
| [beyond_modify_processor_attribute](tools/beyond_modify_processor_attribute.json) | `attribute_id`, `updates` | declared |
| [beyond_delete_models](tools/beyond_delete_models.json) | `model_ids` | declared |
| [beyond_delete_objects](tools/beyond_delete_objects.json) | `object_ids` | declared |
| [beyond_delete_attributes](tools/beyond_delete_attributes.json) | `attribute_ids` | declared |
| [beyond_delete_constraints](tools/beyond_delete_constraints.json) | `constraint_ids` | declared |
| [beyond_delete_relationships](tools/beyond_delete_relationships.json) | `relationship_ids` | declared |

## Transformations and lineage

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_add_transformation_by_sql](tools/beyond_add_transformation_by_sql.json) | `processor_id`, `sql` | declared |
| [beyond_get_transformations](tools/beyond_get_transformations.json) | `processor_id` | declared |
| [beyond_delete_transformations](tools/beyond_delete_transformations.json) | `transformation_ids` | declared |
| [beyond_reorder_transformations](tools/beyond_reorder_transformations.json) | `processor_id`, `transformation_order` | declared |
| [beyond_get_lineage](tools/beyond_get_lineage.json) | — | not declared |

## Security findings

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_add_security_findings](tools/beyond_add_security_findings.json) | `findings` | declared |
| [beyond_list_security_findings](tools/beyond_list_security_findings.json) | — | declared |
| [beyond_modify_security_finding](tools/beyond_modify_security_finding.json) | `finding_id`, `updates` | declared |
| [beyond_delete_security_findings](tools/beyond_delete_security_findings.json) | `finding_ids` | declared |
| [beyond_record_security_scan](tools/beyond_record_security_scan.json) | `findings`, `scope`, `detected_by` | declared |

## Development planning

| Tool | Top-level required | Output schema |
| --- | --- | --- |
| [beyond_get_development_planning_guide](tools/beyond_get_development_planning_guide.json) | — | not declared |
| [beyond_list_development_plans](tools/beyond_list_development_plans.json) | — | not declared |
| [beyond_get_development_plan](tools/beyond_get_development_plan.json) | `dev_plan_id` | not declared |
| [beyond_create_development_plan](tools/beyond_create_development_plan.json) | `plan` | not declared |
| [beyond_update_development_plan](tools/beyond_update_development_plan.json) | `dev_plan_id`, `updates` | not declared |
| [beyond_list_requirements](tools/beyond_list_requirements.json) | — | not declared |
| [beyond_get_requirement](tools/beyond_get_requirement.json) | `requirement_code` | not declared |
| [beyond_create_requirements](tools/beyond_create_requirements.json) | `requirements` | not declared |
| [beyond_update_requirements](tools/beyond_update_requirements.json) | `requirements` | not declared |
| [beyond_list_requirement_reviews](tools/beyond_list_requirement_reviews.json) | `requirement_code` | not declared |
| [beyond_create_requirement_review](tools/beyond_create_requirement_review.json) | `requirement_code`, `review_content` | not declared |
| [beyond_update_requirement_review](tools/beyond_update_requirement_review.json) | `req_review_id`, `review_content` | not declared |
| [beyond_delete_requirement_review](tools/beyond_delete_requirement_review.json) | `req_review_id` | not declared |
| [beyond_list_development_items](tools/beyond_list_development_items.json) | — | not declared |
| [beyond_get_development_item](tools/beyond_get_development_item.json) | `dev_item_id` | not declared |
| [beyond_create_development_items](tools/beyond_create_development_items.json) | `items` | not declared |
| [beyond_update_development_items](tools/beyond_update_development_items.json) | `items` | not declared |
| [beyond_link_requirement_development_items](tools/beyond_link_requirement_development_items.json) | `links` | not declared |
| [beyond_unlink_requirement_development_items](tools/beyond_unlink_requirement_development_items.json) | `links` | not declared |
| [beyond_list_development_analyses](tools/beyond_list_development_analyses.json) | — | not declared |
| [beyond_get_development_analysis](tools/beyond_get_development_analysis.json) | `analysis_code` | not declared |
| [beyond_create_development_analysis](tools/beyond_create_development_analysis.json) | `analysis` | not declared |
| [beyond_update_development_analysis](tools/beyond_update_development_analysis.json) | `analysis_code`, `updates` | not declared |
