import cv2
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

from utils.violations import log_violation

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

away_start_time = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    attention = "No Face"

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            mp.solutions.drawing_utils.draw_landmarks(
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION
            )

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
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    # Attention Monitoring

    if attention in ["Looking Left", "Looking Right"]:

        if away_start_time is None:
            away_start_time = time.time()

        away_duration = time.time() - away_start_time

        cv2.putText(
            frame,
            f"Away: {int(away_duration)}s",
            (30, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        if away_duration > 5:

            log_violation(
                "Praise",
                "Inattentive"
            )

            cv2.putText(
                frame,
                "ATTENTION WARNING",
                (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

    else:

        away_start_time = None

    cv2.imshow(
        "Attention Monitoring",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()