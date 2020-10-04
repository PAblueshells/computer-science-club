import cv2
import face_recognition

vc = cv2.VideoCapture(0)

faces = []

while True:
    ret, frame = vc.read()
    rgb_frame = frame[:, :, ::-1]

    faces = face_recognition.faces(rgb_frame)

    for y2, x2, y1, x1 in faces:
        cv2.rectangle(frame, (x1, y2), (x2, y1), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
