# OpenEMR-based HIS Testbed Architecture (Course)

This testbed represents a mission-critical socio-technical HIS centered on OpenEMR.
OpenEMR is a fixed baseline and MUST NOT be modified.

## Components
- OpenEMR application server (clinical workflows)
- MariaDB (clinical data store)
- External interfaces exposed for student tools:
  1) Database views (read-only analytics)
  2) Audit export channel (JSONL)
  3) Reports / exports (OpenEMR UI reporting + file artifacts)
  4) FHIR API (standards-based interoperability boundary)

## Student work location
Student-developed cybersecurity/trust tools run OUTSIDE OpenEMR and consume only those interfaces.
They produce decision-support and governance outputs (alerts, risk indicators, evidence, policies).
