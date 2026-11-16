# Requirements, planning and analysis

Planning responses already embed current-stage and conditional next-stage guidance; read it. `beyond_get_development_planning_guide(section=...)` is optional extra detail, not a universal prerequisite. Supported sections are start, interview, requirements, reviews, items, estimation, confidence and report.

## Intake

For authorized project setup or requirements registration with supplied Excel/doc/chat requirements: inspect existing plans/requirements and prior agreements, deduplicate, save traceable DRAFT requirements within scope, verify saved IDs, then ask only unanswered gaps. Do not stop at acknowledging the document. Reading or summarizing alone does not authorize writes. If no requirements were supplied, offer an interview and reuse accepted interview plans and answered questions.

Review `about_this_system` and `overall_architecture` documents and returned readiness guidance. SYSTEM authorship is a hint to inspect a template, not proof that it is empty. Distinguish user decisions, source facts, assumptions and questions. Do not invent approval. Ask short questions in the user's language.

## Requirements and discussions

Keep project-wide requirement codes stable and requirements distinct/testable. Preserve existing field conventions; suggested defaults are not enforced enums. `DEV_PHASE` belongs to the requirement; there is no assumed Phase table/tool.

`INTERVIEW_LISTS` holds organized questions/answers as text. Requirement reviews hold participant discussions and replies; they do not have an invented resolution-status workflow. Writes are attributed to AI (MCP) and the authenticated user, not an impersonated participant. Read discussions before reflecting confirmed conclusions in requirements. Parent reviews cannot be deleted while replies exist; edit/delete permissions remain author-bound.

## Work items and forecasts

Break confirmed scope into implementable items with completion conditions and resource forecasts. Link shared work to each applicable requirement but count a `DEV_ITEM_ID` only once overall. For phase allocation, use shares totaling one. `schema_version` is integer 1, not string "1". Person-days are effort, not elapsed duration.

Read latest design before design-based estimation. If no design exists, label the estimate requirements-based, record assumptions/missing design and include design work. Do not claim a design was checked. Design or first implementation can improve evidence only when performed within the user's authorized scope.

Customer `DEV_BUDGET` / `DEV_DURATION_DAYS` are constraints; analysis forecasts are independent estimates. Unknown forecasts are null, not zero. Do not shrink estimates to fit targets. Provide low/recommended/high with currency, workday/calendar-day basis, roles, rates, availability, dependencies, concurrency, testing and contingency. Compare with-AI and without-AI scenarios using consistent scope and explicit evidence. Confidence 0–100 expresses evidence completeness, not calibrated delivery probability.

## Save analysis

Always save full `ANALYSIS_CONTENT` as Markdown even when chat delivery is HTML/PDF/slides. A link, binary/base64 or an HTML document is not a Markdown analysis body. Create a new analysis code for reanalysis; modify an existing report only on explicit user request.

Keep report tables/conclusions, forecast columns and structured `OTHER_INFO` consistent in one save. Only the selected scenario's representative forecasts must match top-level/table forecasts; undecided representative columns stay null. Do not invent historical comparison scenarios. Read the current `report`, `estimation` and `confidence` guide sections before constructing structured forecasts.

Fetch full records after compact write receipts when needed, verify saved IDs and traceability, and report assumptions and unresolved questions. Follow [schema contracts](schema-contracts.md) for large reports and partial responses. Exact payloads are under [the tool index](tools.md).
