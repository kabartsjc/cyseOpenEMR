# OpenEMR Testbed Users (Course)

These accounts are created in OpenEMR via the Admin UI.
They are used to generate realistic access patterns and audit events.

## Accounts
- clinician1  (Role: Clinician)
- admin1      (Role: Admin / Billing)
- itsec1      (Role: IT / Security)

## Intent
Clinicians generate normal clinical activity.
Admin generates billing/reporting workflows.
IT/Security performs maintenance-like actions and audit review.

## Rule (Non-negotiable)
Students MUST NOT change OpenEMR internals. They may only interact with the system
through external interfaces (DB views, audit exports, reports, FHIR).
