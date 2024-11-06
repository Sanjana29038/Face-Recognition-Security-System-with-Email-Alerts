import cv2
import os

def cfd(user_id):
    data_path = 'known_faces/'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{data_path}User.{user_id}.{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Capturing Face Data', frame)
        if cv2.waitKey(1) == 27 or count >= 30:  # ESC key or 30 samples
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captured face data for user {user_id}.")
