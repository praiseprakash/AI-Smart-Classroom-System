import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
import os
from PIL import Image

# -----------------------------
# LOAD KNOWN FACE
# -----------------------------

image_path = r"E:\data_science\AI_Smart_Classroom_System\known_faces\praise.jpeg"

# Open image
img = Image.open(image_path)

# Convert to RGB
img = img.convert("RGB")

# Convert to numpy array
known_image = np.array(img)

# Ensure correct format
known_image = known_image.astype(np.uint8)
known_image = np.ascontiguousarray(known_image)

# Encode known face
known_encoding = face_recognition.face_encodings(known_image)[0]

# Store encoding and name
known_face_encodings = [known_encoding]
known_face_names = ["Praise"]
# _________________________________________________


def mark_attendance(name):
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    file_name = "attendance.csv"

    # Create file if it doesn't exist
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time"])

    already_marked = False

    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) >= 2:
                if row[0] == name and row[1] == today:
                    already_marked = True
                    break

    if not already_marked:
        with open(file_name, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, today, current_time])

        print(f"{name} attendance marked.")
# -----------------------------
# START WEBCAM
# -----------------------------

video_capture = cv2.VideoCapture(0)

while True:

    # Read frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find faces
    face_locations = face_recognition.face_locations(rgb_frame)

    # Encode faces
    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    # Loop through detected faces
    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding
        )

        name = "Unknown"

        # Face distance
        face_distances = face_recognition.face_distance(
            known_face_encodings,
            face_encoding
        )

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            mark_attendance(name)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        # Display name
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    # Show webcam
    cv2.imshow("AI Smart Classroom System", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
video_capture.release()
cv2.destroyAllWindows()