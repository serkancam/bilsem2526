import locale
import os
os.environ["LC_ALL"] = "C"
locale.setlocale(locale.LC_ALL, 'C')

import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.detections:
      for detection in results.detections:
        ih, iw, ic = image.shape
        # 2. Bounding Box verisine ulaş
        bboxc = detection.location_data.relative_bounding_box
        
    if results.detections:
      for detection in results.detections:
        # 1. Görüntü boyutlarını al
        ih, iw, ic = image.shape 
        
        # 2. Bounding Box verisine ulaş
        bboxc = detection.location_data.relative_bounding_box
        
        # 3. Normalize değerleri piksele çevir (Tam sayıya yuvarlayarak)
        x = int(bboxc.xmin * iw)
        y = int(bboxc.ymin * ih)
        w = int(bboxc.width * iw)
        h = int(bboxc.height * ih)
        # mp_drawing.draw_detection(image, detection)
        # İstersen manuel olarak dikdörtgen çizebilirsin:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face=image[y:y+h,x:x+w]
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    cv2.imshow('face', face)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()