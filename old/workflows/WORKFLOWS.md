# Sample Workflows (OpenEMR Testbed)

These workflows are used to generate realistic usage patterns without modifying OpenEMR.
The seeding script creates appointments labeled with these workflows.

## Workflow A: ER Intake & Triage
Goal: register a patient, capture chief complaint, triage, and route to clinician decision support.
Key risks: availability during spikes, hurried authentication, over-collection, misuse of emergency access.

## Workflow B: Outpatient Follow-up (Chronic Care)
Goal: longitudinal record review and documentation with repeat visits over weeks.
Key risks: privacy inference over time, excessive access, role drift (staff turnover).

## Workflow C: Lab Result Review
Goal: order labs and review results, including delayed or missing data.
Key risks: integrity of results, interface trust boundary, delayed care and cascading impacts.

## Workflow D: Medication Refill Request
Goal: refill approval, review of contraindications and recent notes.
Key risks: fraud, unauthorized refill, workflow shortcuts under workload pressure.
