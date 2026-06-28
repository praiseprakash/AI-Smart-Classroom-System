import csv
import os
from datetime import datetime
from utils.database import get_connection

FILE_NAME = "attendance.csv"


def mark_attendance(name):

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    file_exists = os.path.isfile(FILE_NAME)

    
    if file_exists:

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 2:

                    if row[0].lower() == name.lower() and row[1] == today:
                        return

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow(
                ["Name", "Date", "Time"]
            )

        writer.writerow(
            [name, today, current_time]
        )
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    """
        INSERT INTO attendance
        (name, date, time)
        VALUES (?, ?, ?)
        """,
        (name, today, current_time)
    )
    conn.commit()
    conn.close()



    print(f"{name} attendance marked")