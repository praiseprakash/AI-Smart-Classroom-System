import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            # Nose tip
            nose = face_landmarks.landmark[1]

            h, w, _ = frame.shape

            nose_x = int(nose.x * w)

            # Determine direction
            if nose.x < 0.42:
                direction = "Looking Left"

            elif nose.x > 0.58:
                direction = "Looking Right"

            else:
                direction = "Looking Forward"

            cv2.putText(
                frame,
                direction,
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.circle(
                frame,
                (nose_x, int(nose.y * h)),
                5,
                (0, 0, 255),
                -1
            )

    cv2.imshow("Head Direction Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()