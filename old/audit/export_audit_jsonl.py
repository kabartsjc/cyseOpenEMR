#!/usr/bin/env python3
import os
import time
import json
import argparse
import pymysql

DB_HOST = os.getenv("DB_HOST", "mariadb")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "openemr")
DB_USER = os.getenv("DB_USER", "openemr")
DB_PASSWORD = os.getenv("DB_PASSWORD", "openemrpass")
INTERVAL = int(os.getenv("EXPORT_INTERVAL_SEC", "30"))

def conn():
    return pymysql.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD,
        database=DB_NAME, autocommit=True, charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

def table_exists(cur, t):
    cur.execute("SHOW TABLES LIKE %s", (t,))
    return cur.fetchone() is not None

def main(out_path):
    last_id = 0
    while True:
        try:
            with conn() as c:
                with c.cursor() as cur:
                    # OpenEMR versions differ; "log" is common in many installs
                    if not table_exists(cur, "log"):
                        # If this happens, students still have Apache logs via openemr_logs volume.
                        time.sleep(INTERVAL)
                        continue

                    cur.execute("SELECT COALESCE(MAX(id),0) AS m FROM log")
                    max_id = int(cur.fetchone()["m"])
                    if max_id <= last_id:
                        time.sleep(INTERVAL)
                        continue

                    cur.execute(
                        "SELECT id, date, user, event, comments, patient_id FROM log WHERE id > %s ORDER BY id ASC",
                        (last_id,)
                    )
                    rows = cur.fetchall()
                    if rows:
                        with open(out_path, "a", encoding="utf-8") as f:
                            for r in rows:
                                f.write(json.dumps(r, default=str) + "\n")
                        last_id = rows[-1]["id"]
        except Exception:
            # keep exporter resilient for classrooms
            time.sleep(INTERVAL)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    main(args.out)
