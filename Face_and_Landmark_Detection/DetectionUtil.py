import cv2
import dlib
import os
import numpy as np

class DetectionUtil:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        
    def getFaceRect(self, imageBW):
        
        rects = self.detector(imageBW, 1)
        
        if (len(rects) <= 0):
            return -1, None
        
        rect = rects[0]
        
        return 0, rect
    
    def getFlattenedRectangleFromDLibRectangle(self, rect):
        return (rect.left(), rect.top(), rect.right() - rect.left(), rect.bottom() - rect.top())
    
    def shape_to_np(self, dlib_shape):
        # Initialize the list of (x,y) coordinates
        coordinates = np.zeros((dlib_shape.num_parts, 2), dtype="int")

        # Loop over all facial landmarks and convert them to a tuple with (x,y) coordinates:
        for i in range(0, dlib_shape.num_parts):
            coordinates[i] = (dlib_shape.part(i).x, dlib_shape.part(i).y)

        # Return the list of (x,y) coordinates:
        return coordinates

    def get_landmarks(self, imageBW, rect):
        modelPath = 'shape_predictor_68_face_landmarks.dat'
        
        if (os.path.isfile(modelPath)) :
            print("loading model")
        else :
            print("model does not exist")
        
        shape = self.predictor(imageBW, rect)
        shape = self.shape_to_np(shape)
        
        return shape
    
    def draw_shape_points(self, image, np_shape):
        # Draw a point on every landmark position:
        for (x, y) in np_shape:
            cv2.circle(image, (x, y), 3, (0, 255, 0), 20)
            
    def normalizelandmarks(self, image, landmarks):
        imageDimensions = image.shape
        imageWidth = imageDimensions[0]
        imageHeight = imageDimensions[1]
        
        landmarks_norm = np.zeros((68, 2), dtype=float)
        
        print("image width and height : ")
        print(imageWidth)
        print(imageHeight)
        
        for i in range(len(landmarks)):
            (x , y) = landmarks[i]
            x /= imageWidth
            y /= imageHeight
            landmarks_norm[i][0] = x
            landmarks_norm[i][1] = y
            
        return landmarks_norm