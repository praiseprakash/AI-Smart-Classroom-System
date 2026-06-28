import mediapipe as mp
import time
import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import cv2
from ultralytics import YOLO
import face_recognition
from PIL import Image
import numpy as np
from utils.violations import log_violation
from utils.attendance import mark_attendance

# Load YOLO
model = YOLO("yolov8n.pt")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

away_start_time = None





# image_path = r"E:\data_science\AI_Smart_Classroom_System\known_faces\praise.jpeg"

# img = Image.open(image_path)
# img = img.convert("RGB")

# known_image = np.array(img)
# known_image = np.ascontiguousarray(known_image)
# # print("Shape:", known_image.shape)
# # print("Dtype:", known_image.dtype)
# known_encoding = face_recognition.face_encodings(known_image)[0]



# known_face_encodings = [known_encoding]
# known_face_names = ["Praise"]


known_face_encodings = []
known_face_names = []

known_faces_folder = r"E:\data_science\AI_Smart_Classroom_System\known_faces"

for file_name in os.listdir(known_faces_folder):

    if file_name.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):

        image_path = os.path.join(
            known_faces_folder,
            file_name
        )

        img = Image.open(image_path).convert("RGB")

        image = np.array(img)
        image = np.ascontiguousarray(image)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:

            known_face_encodings.append(
                encodings[0]
            )

            student_name = os.path.splitext(file_name)[0].title()

            known_face_names.append(
                student_name
            )

            print(
                f"Loaded: {student_name}"
            )
# Start webcam
cap = cv2.VideoCapture(0)
frame_count=0
current_person = "Unknown"

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1


    if frame_count % 5 == 0:
        small_frame = cv2.resize(frame, (640, 480))
        results = model(small_frame,conf=0.25, imgsz=416, verbose=False)
        # results = model(frame, verbose=False)
        


        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                # print(model.names[int(box.cls[0])])
                # print(class_name)
                if class_name == "cell phone":
                    print("PHONE DETECTED")

                if class_name == "cell phone" and current_person != "Unknown":
                    log_violation(current_person, "Phone Usage")
                    # confidence = float(box.conf[0])

                    # print(f"Phone: {confidence:.2f}")

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        2
                    )

                    cv2.putText(
                        frame,
                        "PHONE",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )


    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mesh_results = face_mesh.process(rgb_frame)

    face_locations = face_recognition.face_locations(rgb_frame)

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding
        )

        # current_person = "Unknown"

        # if True in matches:
        #     current_person = "Praise"
        current_person = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            current_person = known_face_names[ match_index]
            mark_attendance(current_person)
        name = current_person


        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )
    h, w, _ = frame.shape

    if mesh_results.multi_face_landmarks:

        for face_landmarks in mesh_results.multi_face_landmarks:

            nose = face_landmarks.landmark[1]

            nose_x = int(nose.x * w)

            center_x = w // 2

            if nose_x < center_x - 80:

                attention = "Looking Left"

            elif nose_x > center_x + 80:

                attention = "Looking Right"

            else:

                attention = "Looking Center"

            cv2.putText(
                frame,
                attention,
                (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

            if attention in ["Looking Left", "Looking Right"]:

                if away_start_time is None:
                    away_start_time = time.time()

                away_duration = time.time() - away_start_time

                cv2.putText(
                    frame,
                    f"Away: {int(away_duration)}s",
                    (30, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                if away_duration > 5 and current_person != "Unknown":

                    log_violation(
                        current_person,
                        "Inattentive"
                    )

            else:

                away_start_time = None

    cv2.imshow("Integrated System", frame)
   

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
