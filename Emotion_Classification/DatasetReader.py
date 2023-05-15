import os
import numpy as np

class DatasetReader:

    def __init__(self):
        self.dataset_file_path = 'emotion_classification_dataset.txt'
        self.file = None
        self.openDatabaseFileForReading()
    
    def openDatabaseFileForReading(self):
        if (os.path.isfile(self.dataset_file_path)):
            print("dataset file exists; opening in read mode")
            self.file = open(self.dataset_file_path, "r")
        else:
            print("dataset file does not exist; create with database writer")
            return
        
    def readNext(self, count):
        loop = 0
        data = np.zeros((count, 137), dtype=float)
        
        while True:
            line = self.file.readline()
            
            if loop >= count:
                break
            if not line:
                break
            
            values = line.split(',')

            for value in values:
                value = float(value)
                
            
            data[loop] = np.array(values)
            
            loop += 1
            
        return data
            
    def dispose(self):
        self.file.close()
            
'''datasetReader = DatasetReader()

array = datasetReader.readNext(3)

for i in range(len(array)):
    print("data " + str(i))
    for j in range(len(array[i])):
        print(str(j) + " : " + str(array[i][j]))'''