from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Smart Classroom API"
    }


@app.get("/attendance")
def get_attendance():

    conn = sqlite3.connect("classroom.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM attendance"
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


@app.get("/violations")
def get_violations():

    conn = sqlite3.connect("classroom.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM violations"
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


@app.get("/stats")
def get_stats():

    conn = sqlite3.connect("classroom.db")

    cursor = conn.cursor()

    attendance_count = cursor.execute(
        "SELECT COUNT(*) FROM attendance"
    ).fetchone()[0]

    violation_count = cursor.execute(
        "SELECT COUNT(*) FROM violations"
    ).fetchone()[0]

    conn.close()

    return {
        "attendance_records": attendance_count,
        "violation_records": violation_count
    }