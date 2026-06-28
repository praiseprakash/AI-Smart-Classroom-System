# 🎓 AI Smart Classroom Monitoring System

## 📖 Overview

The AI Smart Classroom Monitoring System is an AI-powered classroom monitoring application that automates attendance, detects mobile phone usage, monitors student attention, and stores all records in a SQLite database.

The project combines Computer Vision, Deep Learning, and Web APIs to improve classroom management.

---

## ✨ Features

* ✅ Automatic Face Recognition Attendance
* ✅ Multi-Student Recognition
* ✅ Phone Detection using YOLOv8
* ✅ Student Attention Monitoring using MediaPipe
* ✅ Automatic Violation Logging
* ✅ SQLite Database Integration
* ✅ FastAPI REST APIs
* ✅ Streamlit Dashboard

---

## 🛠 Technologies Used

* Python
* OpenCV
* YOLOv8
* Face Recognition
* MediaPipe
* NumPy
* Pillow (PIL)
* SQLite
* FastAPI
* Streamlit

---

## 📂 Project Workflow

Webcam
↓
Face Recognition
↓
Attendance Module
↓
YOLOv8 Phone Detection
↓
MediaPipe Attention Detection
↓
Violation Module
↓
SQLite Database
↓
FastAPI
↓
Dashboard

---

## 📁 Project Structure

AI_Smart_Classroom_System/

├── api/

├── dashboard/

├── known_faces/

├── utils/

├── integrated.py

├── requirements.txt

├── README.md

└── .gitignore

---

## ▶️ How to Run

### Run Integrated System

python integrated.py

### Run FastAPI

uvicorn api.main:app --reload

### Run Streamlit Dashboard

streamlit run dashboard/dashboard.py

---

## 🌐 API Endpoints

| Endpoint    | Description        |
| ----------- | ------------------ |
| /           | Home               |
| /attendance | Attendance Records |
| /violations | Violation Records  |
| /stats      | Statistics         |

---

## 🚀 Future Improvements

* Email Notifications
* Cloud Database
* Mobile Application
* Teacher Analytics Dashboard
* Multi-Camera Support

---

## 👨‍💻 Developed By

Praise
