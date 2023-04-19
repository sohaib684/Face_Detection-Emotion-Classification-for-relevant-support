import os
import cv2


class FaceDetection:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def getFaceRect(self, image):
        imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(imageBW)

        if faces.__len__() <= 0:
            return -1, None

        (x, y, w, h) = faces[0]

        return 0, imageBW[y:y + h, x:x + w]
