# Attribute classifications and security findings

## Attribute metadata

Read live `attribute_security_guide`. `pii_data_type` takes an exact enum name (for example `DRIVER_LICENSE`) independently of `pii_level`. On modification, omission preserves it and null clears it.

`encryption_level` is an integer: 0 NONE, 1 MASKED, 2 ENCRYPTED, 3 HASHED, 4 KEYSERVER. New attributes default to 0; omission on modification preserves; 0 clears; null is rejected. Classification metadata does not encrypt runtime data. Inspect actual implementation before claiming protection.

Use `beyond_find_attributes` with verified filters and top-level `object_types`. A read restricted to some objects/canvases cannot establish project-wide absence. Use classification evidence and the selected guide, not names alone, when assigning values.

## Findings

Read live `security_findings_guide` before writes. Use `beyond_add_security_findings`, `beyond_list_security_findings`, `beyond_modify_security_finding`, `beyond_delete_security_findings` and `beyond_record_security_scan` for their actual contracts. Fingerprints identify findings; findings, target mappings and standard snapshots are saved atomically under the tool's documented scope. Mask secrets in evidence.

Do not submit an automated scanner decision as a human risk acceptance. Automated scan items exclude status, status_reason, accepted_until and branch; branch is supplied at the top level. Default scanner refresh preserves metadata; `refresh_scanner_fields=true` refreshes supplied scanner fields/mappings but preserves human decisions and first-detected history.

## Complete versus partial scans

Only a successful `complete=true` scan can mark absent findings FIXED within its exact explicit rule/file/model scope and branch, and only with required all-canvas access. Never use the last batch of a partial scan as a complete scope. Requests support at most 200 findings: larger scans require exact disjoint scopes, or remain partial.

Reappearing FIXED findings become REOPENED; ACCEPTED_RISK and FALSE_POSITIVE remain unchanged. Restricted access, missing files, failed checks or incomplete analysis do not justify absence reconciliation.

Linked complete scans require an explicitly CHECKED PROJECT root or matching scoped MODEL root. Incremental reconciliation requires exact source-file scope; individual checked nodes do not authorize broader resolution. Use the actual analysis run ID when linking analysis and findings. Read current scan/analysis definitions before setting coverage fields.

Verify saved finding IDs, mappings and scope. Report checked rules/files, unsupported paths, findings and actual resolution decisions separately. No findings does not prove the system is secure.
