import csv
import os
from datetime import datetime
from utils.database import get_connection

FILE_NAME = "violations.csv"

last_logged = {}


def log_violation(name, violation):

    key = f"{name}_{violation}"

    now = datetime.now()

    if key in last_logged:

        diff = (
            now - last_logged[key]
        ).total_seconds()

        if diff < 60:
            return

    last_logged[key] = now

    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Name", "Violation", "Date", "Time"]
            )

        writer.writerow(
            [name, violation, date, time]
        )
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO violations
        (name, violation, date, time)
        VALUES (?, ?, ?, ?)
        """,
        (name, violation, date, time)
    )
    conn.commit()
    conn.close()

    print(f"{name} - {violation} saved")