# External Interfaces Students May Use (Allowed Integration Points)

## 1) Database Views (Read-only)
Use DB user: analytics_ro / analytics_ro_pass
Example:
mysql -h localhost -P 3306 -u analytics_ro -p openemr
SELECT * FROM v_patient_basic LIMIT 5;

## 2) Audit Export (JSONL)
The audit_exporter writes to a shared volume:
exports/audit.jsonl
Students can tail / ingest this file.

## 3) Reports / Exports
Students may generate OpenEMR reports from the UI and treat exported CSV/PDF as inputs
to governance tools (leakage checks, approval workflows, policy validation).

## 4) FHIR API
OpenEMR provides a FHIR endpoint (version-dependent).
Students must treat FHIR as a trust boundary.
Example (after enabling FHIR in OpenEMR globals if needed):
GET http://localhost:8080/apis/fhir/Patient?_count=5
