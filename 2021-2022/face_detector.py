import cv2
import numpy as np
from facenet_pytorch import MTCNN

class FaceDetector(object):
    """
    Face detector class
    """

    def __init__(self, mtcnn, path):
        self.mtcnn = mtcnn
        self.image = cv2.imread(path)

    def _draw(self, frame, boxes, probs, landmarks):
        """
        Draw landmarks and boxes for each face detected
        """
        if boxes is None:
            return frame
        for box, prob, ld in zip(boxes, probs, landmarks):
                # Draw rectangle on frame
            img = cv2.resize(self.image, (int(box[2])-int(box[0]), int(box[3])-int(box[1])))
            frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])] = img
            # cv2.rectangle(frame,
              #            (int(box[0]), int(box[1])),
            #           (int(box[2]), int(box[3])),
             #             (0, 0, 255),2)
        return frame

    def run(self):
        """
            Run the FaceDetector and draw landmarks and boxes around detected faces
        """
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if ret:
                # detect face box, probability and landmarks
                boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True)
                # draw on frame
                print(boxes, frame.shape)
                self._draw(frame, boxes, probs, landmarks)
            # Show the frame
            cv2.imshow('Detected Face',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        
# Run the app
mtcnn = MTCNN()
fcd = FaceDetector(mtcnn, 'bunny.png')
fcd.run()
