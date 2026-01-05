-- Create a read-only analytics user for student tools (DB interface)
CREATE USER IF NOT EXISTS 'analytics_ro'@'%' IDENTIFIED BY 'analytics_ro_pass';
GRANT SELECT ON openemr.* TO 'analytics_ro'@'%';

-- Minimal views (stable, easy to reason about)
CREATE OR REPLACE VIEW v_patient_basic AS
SELECT
  pid,
  pubpid,
  fname,
  lname,
  DOB,
  sex,
  city,
  state,
  postal_code
FROM patient_data;

CREATE OR REPLACE VIEW v_patient_contact AS
SELECT
  pid,
  phone_home,
  email,
  street,
  city,
  state,
  postal_code,
  country_code
FROM patient_data;

-- Appointments view (supports workflow analysis)
CREATE OR REPLACE VIEW v_appointments AS
SELECT
  pc_eid AS event_id,
  pc_pid AS pid,
  pc_title,
  pc_eventDate,
  pc_startTime,
  pc_endTime,
  pc_apptstatus
FROM openemr_postcalendar_events;

FLUSH PRIVILEGES;
