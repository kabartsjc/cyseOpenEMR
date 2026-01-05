#!/usr/bin/env python3
import os
import random
import time
from datetime import datetime, timedelta, date

import pymysql
from faker import Faker

DB_HOST = os.getenv("DB_HOST", "mariadb")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "openemr")
DB_USER = os.getenv("DB_USER", "openemr")
DB_PASSWORD = os.getenv("DB_PASSWORD", "openemrpass")

SEED_PATIENTS = int(os.getenv("SEED_PATIENTS", "80"))
RANDOM_SEED = int(os.getenv("RANDOM_SEED", "587"))

random.seed(RANDOM_SEED)
fake = Faker()
fake.seed_instance(RANDOM_SEED)

def conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

def wait_for_tables(timeout_sec=300):
    deadline = time.time() + timeout_sec
    required = {"patient_data", "openemr_postcalendar_events"}
    while time.time() < deadline:
        try:
            with conn() as c:
                with c.cursor() as cur:
                    cur.execute("SHOW TABLES")
                    tables = {list(r.values())[0] for r in cur.fetchall()}
                    if required.issubset(tables):
                        return
        except Exception:
            pass
        time.sleep(5)
    raise RuntimeError("OpenEMR tables not ready. Ensure OpenEMR finished initializing.")

def next_pid(cur):
    cur.execute("SELECT COALESCE(MAX(pid), 0) AS m FROM patient_data")
    return int(cur.fetchone()["m"]) + 1

def insert_patient(cur, pid):
    sex = random.choice(["Male", "Female"])
    dob = fake.date_of_birth(minimum_age=0, maximum_age=90)
    cur.execute(
        """
        INSERT INTO patient_data
        (pid, pubpid, fname, lname, DOB, sex, phone_home, email, street, city, state, postal_code, country_code)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            pid,
            f"SYN-{pid:06d}",
            fake.first_name_male() if sex == "Male" else fake.first_name_female(),
            fake.last_name(),
            dob,
            sex,
            fake.phone_number()[:20],
            fake.email(),
            fake.street_address()[:60],
            fake.city()[:30],
            fake.state_abbr(),
            fake.postcode()[:10],
            "US",
        ),
    )

def insert_appointment(cur, pid, title, days_from_now, duration_min=30):
    start = datetime.now() + timedelta(days=days_from_now, hours=random.randint(8, 16))
    end = start + timedelta(minutes=duration_min)

    cur.execute(
        """
        INSERT INTO openemr_postcalendar_events
        (
          pc_catid,
          pc_aid,
          pc_pid,
          pc_title,
          pc_eventDate,
          pc_startTime,
          pc_endTime,
          pc_apptstatus,
          pc_multiple,
          pc_recurrtype,
          pc_recurrspec
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            1,          # pc_catid (general appointment)
            1,          # pc_aid (admin/provider placeholder)
            pid,
            title,
            start.date(),
            start.time().strftime("%H:%M:%S"),
            end.time().strftime("%H:%M:%S"),
            "-",        # appointment status
            0,          # pc_multiple (NOT NULL)
            0,          # pc_recurrtype (no recurrence)
            ""          # pc_recurrspec
        ),
    )


def main():
    wait_for_tables()
    with conn() as c:
        with c.cursor() as cur:
            pid = next_pid(cur)

            for i in range(SEED_PATIENTS):
                insert_patient(cur, pid + i)

            # Sample workflow appointment patterns
            # (1) ER Intake (some same-day / next-day)
            # (2) Outpatient Follow-up (1–30 days)
            # (3) Lab Result Review (2–14 days)
            # (4) Medication Refill Request (0–7 days)
            for i in range(SEED_PATIENTS):
                this_pid = pid + i
                if random.random() < 0.35:
                    insert_appointment(cur, this_pid, "ER Intake - SYN", random.randint(0, 2), 60)
                insert_appointment(cur, this_pid, "Outpatient Visit - SYN", random.randint(1, 30), 30)
                if random.random() < 0.55:
                    insert_appointment(cur, this_pid, "Lab Result Review - SYN", random.randint(2, 14), 20)
                if random.random() < 0.25:
                    insert_appointment(cur, this_pid, "Medication Refill - SYN", random.randint(0, 7), 15)

    print(f"Seeded {SEED_PATIENTS} synthetic patients and appointments.")

if __name__ == "__main__":
    main()
