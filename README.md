# 🎓 AI Smart Classroom Monitoring System

## 📌 Project Overview

The **AI Smart Classroom Monitoring System** is a Computer Vision and Deep Learning project that automates classroom monitoring using artificial intelligence. The system recognizes students, marks attendance automatically, detects mobile phone usage, monitors student attention, stores records in a SQLite database, provides REST APIs using FastAPI, and displays analytics through a Streamlit dashboard.

This project demonstrates the integration of multiple AI technologies into a single real-time classroom monitoring solution.

---

## ✨ Features

* 👤 Automatic Face Recognition Attendance
* 📱 Mobile Phone Detection using YOLOv8
* 👀 Student Attention Monitoring using MediaPipe Face Mesh
* 📝 Automatic Attendance Logging
* ⚠️ Automatic Violation Logging
* 🗄️ SQLite Database Integration
* 🌐 FastAPI REST APIs
* 📊 Interactive Streamlit Dashboard

---

## 🛠️ Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* Face Recognition
* MediaPipe
* NumPy
* Pillow (PIL)
* SQLite
* FastAPI
* Streamlit

---

## 🔄 Project Workflow

1. Capture live video from the webcam.
2. Recognize students using Face Recognition.
3. Mark attendance automatically (once per day).
4. Detect mobile phone usage using YOLOv8.
5. Monitor head direction using MediaPipe Face Mesh.
6. Log inattentive behavior if the student looks away for more than 5 seconds.
7. Store attendance and violations in CSV files and SQLite database.
8. Access stored records through FastAPI endpoints.
9. Visualize attendance and violation statistics in the Streamlit dashboard.

---

## 📂 Project Structure

```text
AI_Smart_Classroom_System/
│
├── api/
│   └── main.py
├── dashboard/
│   └── dashboard.py
├── known_faces/
├── utils/
│   ├── attendance.py
│   ├── violations.py
│   └── database.py
├── integrated.py
├── attendance.csv
├── violations.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Smart-Classroom-System.git
cd AI-Smart-Classroom-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run the Integrated AI System

```bash
python integrated.py
```

### Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to test the APIs.

### Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 🌐 API Endpoints

| Endpoint      | Description                              |
| ------------- | ---------------------------------------- |
| `/`           | API Home                                 |
| `/attendance` | View attendance records                  |
| `/violations` | View violation records                   |
| `/stats`      | View attendance and violation statistics |

---

## 📊 Database

The project stores data in a **SQLite** database (`classroom.db`) and also maintains CSV files for easy viewing.

### Attendance Table

* id
* name
* date
* time

### Violations Table

* id
* name
* violation
* date
* time

---

## 📸 Outputs



* Face Recognition
* Phone Detection
* Attention Detection
* FastAPI Documentation
* Streamlit Dashboard

---

## 🚀 Future Enhancements

* Multi-camera classroom monitoring
* Cloud database integration
* Email or SMS alerts
* Student performance analytics
* Teacher login and authentication
* Mobile application support

---

## 👨‍💻 Author

**Praise Prakash**

Artificial Intelligence & Data Science Student

This project was developed as an academic portfolio project to demonstrate practical applications of Computer Vision, Deep Learning, REST APIs, and Dashboard development.
