
import cv2
from deepface import DeepFace  # Make sure to install DeepFace first with pip install deepface


try:
    known_faces = DeepFace.find(db_path="D:/facial reg/known_faces", model_name="VGG-Face")
except Exception as e:
    print(f"Error loading known faces: {e}")
    known_faces = None
def rtm():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    def send_alert():
        print("Alert: Unknown person detected!")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            try:
                # Attempt to recognize the face using DeepFace
                result = DeepFace.find(face, db_path="D:/facial reg/known_faces", model_name="VGG-Face")
                if len(result) > 0:
                    user_name = result.iloc[0]['identity']
                    confidence = 100 - result.iloc[0]['VGG-Face_cosine']
                    cv2.putText(frame, f"{user_name} - {round(confidence)}%", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                else:
                    send_alert()
                    cv2.putText(frame, "Unknown", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            except:
                send_alert()
                cv2.putText(frame, "Unknown", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Recognition Security System', frame)
        if cv2.waitKey(1) == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

rtm()
