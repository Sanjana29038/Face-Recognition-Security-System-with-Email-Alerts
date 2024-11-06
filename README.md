Face-Recognition-Security-System-with-Email-Alerts

This project implements a Face Recognition Security System that uses computer vision techniques to detect and recognize faces from real-time video streams. When an unknown face is detected, the system sends an email alert to a predefined email address, ensuring immediate notification of potential intrusions.

The system leverages VGG-Face, a pre-trained deep learning model, for face recognition. The model compares faces in real-time against a database of known faces to verify the identity. If no match is found, an email alert is triggered to notify the owner about the intrusion.

Key Features
Real-time Face Detection: Uses OpenCV’s Haar Cascade Classifier to detect faces in video frames.
Face Recognition with DeepFace: Uses the VGG-Face model for recognizing faces against a local database of known faces.
Email Alert System: Sends an email notification when an unknown face is detected, using Python’s smtplib and environment variables for security.
Known Face Database: Stores known faces in a folder (e.g., known_faces/), which the system uses to match against incoming faces.
Technologies Used
Python: Core programming language.
OpenCV: For real-time video capture and face detection.
DeepFace: For facial recognition using the VGG-Face model.
smtplib: To send email alerts in case of detection of an unknown face.
dotenv: For securely managing email credentials.
How to Run
Clone this repository to your local machine.
Install the required libraries:
bash
Copy code
pip install opencv-python deepface smtplib python-dotenv
Place your test images in the known_faces/ folder.
Set up a .env file in the project root with the following content:
makefile
Copy code
EMAIL_PASSWORD=your_email_password
Run the main script:
bash

The system will continuously monitor the video stream from your camera, detect faces, and compare them with the known faces database. If an unknown face is detected, an email will be sent to the specified recipient.
