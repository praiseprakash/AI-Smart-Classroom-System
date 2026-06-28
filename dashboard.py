# import streamlit as st
# import sqlite3
# import pandas as pd

# st.set_page_config(
#     page_title="AI Smart Classroom Dashboard",
#     page_icon="🎓",
#     layout="wide"
# )

# st.title("🎓 AI Smart Classroom Dashboard")

# conn = sqlite3.connect("classroom.db")

# attendance_df = pd.read_sql_query(
#     "SELECT * FROM attendance",
#     conn
# )

# violations_df = pd.read_sql_query(
#     "SELECT * FROM violations",
#     conn
# )

# conn.close()

# # =========================
# # Metrics
# # =========================

# total_students = attendance_df["name"].nunique()

# phone_count = len(
#     violations_df[
#         violations_df["violation"] == "Phone Usage"
#     ]
# )

# inattentive_count = len(
#     violations_df[
#         violations_df["violation"] == "Inattentive"
#     ]
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(
#         "Students Present",
#         total_students
#     )

# with col2:
#     st.metric(
#         "Phone Violations",
#         phone_count
#     )

# with col3:
#     st.metric(
#         "Inattentive Violations",
#         inattentive_count
#     )

# # =========================
# # Attendance Table
# # =========================

# st.subheader("📋 Attendance Records")

# st.dataframe(
#     attendance_df,
#     use_container_width=True
# )

# # =========================
# # Violation Table
# # =========================

# st.subheader("🚨 Violation Records")

# st.dataframe(
#     violations_df,
#     use_container_width=True
# )

# # =========================
# # Student Statistics
# # =========================

# st.subheader("📊 Student Statistics")

# if not violations_df.empty:

#     stats = (
#         violations_df
#         .groupby(["name", "violation"])
#         .size()
#         .unstack(fill_value=0)
#     )

#     st.dataframe(
#         stats,
#         use_container_width=True
#     )

# # =========================
# # Charts
# # =========================

# if not violations_df.empty:

#     st.subheader("📈 Violations by Student")

#     chart_data = (
#         violations_df
#         .groupby("name")
#         .size()
#     )

#     st.bar_chart(chart_data)










import streamlit as st
import sqlite3
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

st.set_page_config(
page_title="AI Smart Classroom Dashboard",
page_icon="🎓",
layout="wide"
)

st.title("🎓 AI Smart Classroom Dashboard")

# Database Connection

conn = sqlite3.connect("classroom.db")

attendance_df = pd.read_sql_query(
"SELECT * FROM attendance",
conn
)

violations_df = pd.read_sql_query(
"SELECT * FROM violations",
conn
)

conn.close()

# Metrics

students_present = (
attendance_df["name"].nunique()
if not attendance_df.empty
else 0
)

phone_violations = len(
violations_df[
violations_df["violation"] == "Phone Usage"
]
)

inattentive_violations = len(
violations_df[
violations_df["violation"] == "Inattentive"
]
)

col1, col2, col3 = st.columns(3)

col1.metric(
"Students Present",
students_present
)

col2.metric(
"Phone Violations",
phone_violations
)

col3.metric(
"Inattentive Violations",
inattentive_violations
)

# Attendance Table

st.subheader("📋 Attendance Records")

st.dataframe(
attendance_df,
use_container_width=True
)

# Violations Table

st.subheader("🚨 Violation Records")

st.dataframe(
violations_df,
use_container_width=True
)

# Violations Chart

if not violations_df.empty:
    st.subheader("📊 Violations by Student")

    chart_data = (
        violations_df
        .groupby("name")
        .size()
    )

st.bar_chart(chart_data)