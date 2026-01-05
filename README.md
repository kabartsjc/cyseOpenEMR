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

      docker compose down -v --remove-orphans
      docker container prune -f
      docker volume prune -f
      docker image prune -a -f
  
      docker compose up -d
    
      docker ps # wait for all the services is healthy

      
      You must see: 

          - openemr_mariadb healthy

          - openemr_app healthy
      
---

### 9) Accessing the System

Open a browser and navigate to:

HTTP: http://localhost:8080

HTTPS: https://localhost:8443

Login credentials: admin / pass

---

# OpenEMR Minimal Working Setup

Goal

- 2 Clinics (Facilities)

- 2 Doctors (Providers + Login users)

- 5 Patients

Appointments visible in the Calendar

- Starting point:

- Fresh OpenEMR

- Only admin user exists

## 1) Create the Clinics (Facilities)

Menu Option: Admin --> Clinic --> Facilities

Create two facilities:

### Facility 1

  - Name: SYN Clinic 1

  - Address: anything

  - Country / State: select something

### Facility 2

  - Name: SYN Clinic 2

Click Save for each.


## 2) Create the Doctors (Users + Providers)

⚠️ Doctors must be users, not just database entries.

Menu Option: Admin --> Users

### Doctor 1

  - Username: doctor1

  - Password: Doctor@2026

  - Role: Clinician

  - First Name / Last Name

  - Check these boxes:

        ☑ Provider

        ☑ Calendar

        ☑ Active

Click Save

### Doctor 2

    - Username: doctor2

    - Password: Doctor@2026

    - Role: Clinician

    - Check:

          ☑ Provider

          ☑ Calendar

          ☑ Active

    Click Save


