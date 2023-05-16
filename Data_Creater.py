from Face_and_Landmark_Detection.ExtractionUtil import ExtractionUtil
from Emotion_Classification.DatasetWriter import DatasetWriter
import cv2
import numpy as np
import os

extractionUtil = ExtractionUtil()
datasetWriter = DatasetWriter()

dataset_folder = 'data'

# Define the emotions and their corresponding folder names
emotions = ['surprise', 'sad','neutral','happy','fear','disgust','angry']  # Add more emotions as needed

for i, emotion in enumerate(emotions):
    emotion_folder = os.path.join(dataset_folder, emotion)
    image_files = os.listdir(emotion_folder)

    for image_file in image_files:
        image_path = os.path.join(emotion_folder, image_file)
        image = cv2.imread(image_path)

        imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        ret, rect = extractionUtil.getFaceRect(imageBW)

        if ret == -1:
            pass
            # print("No face detected")
        else:
            cv2.rectangle(image, extractionUtil.getFlattenedRectangleFromDLibRectangle(rect), (0, 0, 255), 10)

            landmarks = extractionUtil.get_landmarks(imageBW, rect)
            extractionUtil.draw_shape_points(image, landmarks)

            waitKeyRet = cv2.waitKey(1)

            datasetWriter.addNewData(landmarks, i+1)  # Pass folder number instead of index

        image = cv2.resize(image, (600, 600))
        cv2.imshow("window", image)

        waitKeyRet = cv2.waitKey(1)

        if waitKeyRet & 0xFF == ord('q'):
            break

    if waitKeyRet & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
datasetWriter.dispose()
