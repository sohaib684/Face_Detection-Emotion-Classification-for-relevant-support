import cv2

class FacDetection :
    def __init__() :
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    def loadImages(self, path) :
        images = []
        for filename in os.listdir(path) :
            img = cv2.imread(os.path.join(path, filename))
            if img is not None :
                images.append(img)
        return images