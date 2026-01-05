# OpenEMR Cybersecurity Systems Engineering Testbed  
## Student Guide

This repository provides access to a **preconfigured Healthcare Information System (HIS)** based on **OpenEMR**, used throughout the course **Cybersecurity Systems Engineering**.

You will use this system as a **realistic, mission-critical clinical platform** to design and prototype **external cybersecurity, privacy, trust, and governance tools**.

This environment reflects **real-world constraints** found in healthcare systems and is intentionally designed to support **systems thinking**, not software patching.

---

## 1. Purpose of the Testbed

The OpenEMR testbed represents a **hospital information system already in operation**.  
It includes:

- Real OpenEMR software
- Synthetic (non-real) patient data
- Clinical workflows and scheduling
- Configured clinical providers
- Audit logging
- Standards-based interfaces (FHIR)

You should treat this system as if it were **owned by a hospital**, not by you.

---

## 2. Your Role in This Project

You are acting as a:

**Cybersecurity Systems Engineer / Architect**

Your role is **not** to modify or “fix” OpenEMR, but to:

- Observe the system as it exists
- Identify security, privacy, trust, or governance gaps
- Reason about risks and constraints
- Design and prototype **external tools** that add value

Your final deliverable is a **proof-of-concept (PoC)** demonstrating **insight, feasibility, and value**, not a production-ready system.

---

## 3. What You Are Allowed to Do

You may:

- Log into the OpenEMR web interface using credentials provided by the instructor
- Explore patient records, encounters, workflows, and scheduling
- Consume data via **external interfaces**, including:
  - FHIR endpoints
  - Audit log exports
  - Read-only database views
- Build **external tools or services**, such as:
  - Security monitoring dashboards
  - Privacy risk analyzers
  - Anomaly or misuse detection
  - Compliance and governance reporting
  - Trust or accountability scoring

Your tools may be implemented in **any programming language or framework**.

---

## 4. What You Are NOT Allowed to Do

You must not:

- Modify OpenEMR source code
- Change database schemas or tables
- Edit OpenEMR configuration files
- Install OpenEMR plugins or extensions
- Bypass authentication or authorization
- Directly manipulate clinical records

If something in the system appears confusing or unintuitive, assume:

## 5.Environment Preparation (Windows)

### 1) Prepare the WSL to run the project. In the terminal run this command:

    wsl --install -d Ubuntu

### 2) Define Ubuntu as the main distribution

    wsl --set-default Ubuntu

    wsl --list --verbose

### 3) In the VS Code

    - Type Ctrl + Shift + P

    - Select  “WSL: Connect to WSL”

#### 4) In the wsl shell, clone the repo

    git clone https://github.com/kabartsjc/cyseOpenEMR.git


### 5) Enter in the Docker Windows configuration 

    - Click on Settings --> Resources → WSL Integration --> Enable integration with my default WSL distro --> Ubuntu
    - Restart Docker

    - check if the changes work
        
        docker version
        
        docker compose version

    - Add the user to have permissions in Docker

        sudo usermod -aG docker $USER

### 7) In the Windows terminal, run these commands

    wsl --shutdown

    wsl

    - wait few seconds and reopen the vscode


### 8) Run the Docker compose commands
    
     docker compose up -d

     docker compose ps

     You must see: 

      - openemr_mariadb healthy

      - openemr_app healthy
---

## 9) Accessing the System

Open a browser and navigate to:

HTTP: http://localhost:8080

HTTPS: https://localhost:8443

Login credentials: admin / pass

---

## 10) Log of the system

    docker logs openemr_app --tail=100

    docker logs openemr_mariadb --tail=100


### A. FHIR API

FHIR provides standardized access to clinical data.

Example:
http://localhost:8080/fhir/Patient

You can use FHIR to analyze data exposure, assess privacy and interoperability risks, and build read-only analytics tools.

### B. Audit Logs

Audit events are exported outside OpenEMR and record:

- User logins
- Access to patient records
- System actions
- Timestamps and roles

Audit logs are central to security monitoring, misuse detection, and governance.

### C. Read-Only Database Views

Some read-only database views are exposed for analytics purposes.

You may query aggregated or observational data, but you may not write to the database or alter clinical data.

---

## 7. Project Scope and Creativity

The project scope is intentionally open-ended.

Illustrative examples include:

- Detecting anomalous access to patient records
- Analyzing privacy risks across workflows
- Identifying role misuse or privilege creep
- Governance dashboards for compliance officers
- Socio-technical risk analysis
- Trust and explainability assessment

You are encouraged to propose your own innovative idea.

---

## 8. Proof-of-Concept Expectations

Your PoC should:

- Clearly describe the problem being addressed
- Explain why the problem matters
- Show how your tool consumes system data and produces insight
- Demonstrate feasibility
- Discuss assumptions, trade-offs, and limitations

Reasoning and system understanding matter more than code volume.

---

## 9. Final Reminder

This testbed is not about breaking OpenEMR.

It is about understanding complex socio-technical systems and designing responsible, realistic cybersecurity solutions.

Approach this project as if your solution could one day be evaluated for deployment in a real hospital.
