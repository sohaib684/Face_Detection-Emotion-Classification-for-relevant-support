from io import TextIOWrapper
import os
import numpy as np

class DatasetWriter:
    emotion_labels = ['happy', 'sad', 'anger', 'fear', 'neutral', 'surprise', 'disgust']
    emotion_keybinds = ['1', '2', '3', '4', '5', '6', '7']
    
    def __init__(self):
        self.dataset_file_path = 'emotion_classification_dataset.txt'
        self.file = None
        self.openDatabaseFileForWriting()
    
    def openDatabaseFileForWriting(self):
        if (os.path.isfile(self.dataset_file_path)):
            print("dataset file exists; opening in append mode")
            self.file = open(self.dataset_file_path, "a")
        else:
            print("dataset file does not exist; creating new file")
            self.file = open(self.dataset_file_path, "x")
        
    def addNewData(self, landmarks, emotion_label : int):
        if (len(landmarks) != 136):
            print("Dataset Manager : landmark data is not properly formed for entry; Shape is :")
            print(np.shape(landmarks))
            exit()
            
        for i in range(len(landmarks)):
            self.file.write(str(landmarks[i]))
            self.file.write(",")
        self.file.write(str(emotion_label))
        self.file.write("\n")
        
        print("new landmark data is saved against label : " + self.emotion_labels[emotion_label])
        
    def dispose(self):
        self.file.close()