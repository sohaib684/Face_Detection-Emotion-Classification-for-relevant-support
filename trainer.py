
from Face_and_Landmark_Detection.ExtractionUtil import ExtractionUtil
from Emotion_Classification.DatasetWriter import DatasetWriter
import cv2
import numpy as np

extractionUtil = ExtractionUtil()
datasetWriter = DatasetWriter()

vid = cv2.VideoCapture(1)

while True:
    ret, image = vid.read()
    
    imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ret, rect = extractionUtil.getFaceRect(imageBW)

    if ret == -1:
        pass
        #print("No face detected")
    else:

        cv2.rectangle(image, extractionUtil.getFlattenedRectangleFromDLibRectangle(rect), (0, 0, 255), 10)

        landmarks = extractionUtil.get_landmarks(imageBW, rect)
        extractionUtil.draw_shape_points(image, landmarks)
        
        waitKeyRet = cv2.waitKey(1)
        
        for i in range(len(datasetWriter.emotion_keybinds)):
            ch = datasetWriter.emotion_keybinds[i]
            
            if waitKeyRet & 0xFF == ord(ch):
                landmarks = extractionUtil.normalizelandmarks(image, landmarks)
                landmarks = np.reshape(landmarks, (136))
                
                datasetWriter.addNewData(landmarks, i)
                break

    image = cv2.resize(image, (600, 600))
    cv2.imshow("window", image)
    
    waitKeyRet = cv2.waitKey(1)
            
    if waitKeyRet & 0xFF == ord('q'):
        break
        
    #print("running program")
  
vid.release()
cv2.destroyAllWindows()
datasetWriter.dispose()