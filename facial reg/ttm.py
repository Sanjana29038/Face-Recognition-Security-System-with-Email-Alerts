import numpy as np
import cv2
import os

def ttm():
    data_path = 'known_faces/'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, labels = [], []

    for filename in os.listdir(data_path):
        label = int(filename.split(".")[1])
        img_path = os.path.join(data_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        faces.append(img)
        labels.append(label)

    recognizer.train(faces, np.array(labels))
    recognizer.save('face_trained.yml')
    print("Training complete!")
