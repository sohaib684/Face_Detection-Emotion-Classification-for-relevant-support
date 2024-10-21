# CU_BTECH_PROJECT
This is a Project built with the help of 2 members on Facial Expression repot analysis.
## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Dataset Description](#dataset-description)
3. [Installation](#installation)
4. [Methodology](#methodology)
7. [Results](#results)
8. [Model Demo](#model-demo)

## Problem Statement
Human Facial Expression can be mainly classified into roughly seven kinds of emotions namely happy, sad, surprise, fear, anger, disgust, and neutral, although most of the time there are mix of emotional states.These complex emotions can often contain an abundant amount of information about people’s state of mind and body.
Different organizations and companies can analyze these informations to provide various services, for example retailers may evaluate customer interest, Entertainment producers monitor audience engagement etc.

## Dataset Description

### Note : Face detection dataset : http://vis-www.cs.umass.edu/fddb/index.html#download

## Installation and Tools
Development Tools :
● For faster in-built libraries and user-friendly syntax, we have used Python 3.6 and
OpenCV library for the development.
● Dlib is used as the face detection and landmark extraction library.
● Numpy module of python is also used as the fast and default matrix and array
calculation library.
● We have also used ‘Github.com’ for source control and repository management.
3.3.System Specifications :
Operating System: 64-bit Windows ( Windows 10, Windows 11)
Processor: 64-bit processor
Memory (RAM): 8GB RAM ( DDR4)
Storage: (1TB)
GPU: (specify the desired or minimum graphics card specifications if applicable)
## Methodology
Preprocessing : At first the image data is converted into grayscale image for processing.
Using DLib :
Dlib is a python library for machine learning and networking etc.
We use an internal ‘frontal face detector model’ which is based on HOG and linear SVM.
The rectangle region of detection is then used for landmark extraction.
Although the 48 * 48 resolution images of the FER dataset has been used for the classifier training which were precut.
Reasons for not using a few alternative approaches :
The haar-cascade model based on feature detection and cascade learning is also a fast technique for face detection which  is not used due to incompatibility with the dlib landmark extraction model.
The CNN based face detection of DLib is more robust and accurate than the SVM based model which is also eliminated from the scope because it was computationally heavy against very limited resources and rapid detection.
Common features that can be extracted are,
Lips
Eyes
Eyebrows
Nose-tip
The first step of the system is to detect the face from the dataset images for training and testing and after implementation the task is to detect the face from the camera in real-time or some other input sources.
At the next stage, the ‘shape_predictor_68_face_landmarks.dat‘ model is used for detection 68 landmark coordinate points from the rectangular region of face detection.
Neural Network Approach:The neural network contained a hidden layer with neurons. Each neural network is trained independently with the use of on-line back propagation. 
Step action of one hidden-layer back propagation:
Initialize weights with small random values.
While the stopping condition is not met:
      a. For each training pattern:
Calculate the net input and output of the hidden layer neurons.
Calculate the net input and output of the output layer neurons.
       b. For each output neuron:
Calculate the error term using the derivative of the activation function and the target output.
 Update the weights between the hidden and output layers.
          c. For each hidden neuron:
Calculate the error term using the derivative of the activation function and the weighted      error terms from the output layer.
Update the weights between the input and hidden layers.
    3. Repeat steps 2a-2c until the stopping condition is met

## MODELS :   Use of KNN and SVM:
Both K-Nearest Neighbors (KNN) and Support Vector Machines (SVM) are suitable for datasets with geometric features and a small number of input features.
KNN focuses on identifying similarities among nearest neighbors in the feature space for emotion classification.
SVM aims to find an optimal decision boundary that maximizes the margin between different emotion classes.

##RESULTS
![image](https://github.com/user-attachments/assets/78443a5e-1fff-4674-891f-5e7550906e2a)
![image](https://github.com/user-attachments/assets/3c256560-f983-4cfc-8f19-fb0ed66872d4)
![image](https://github.com/user-attachments/assets/cf6787a1-14da-4eef-806d-513d7fcfe10d)


![image](https://github.com/user-attachments/assets/f0b8d961-92cb-45c6-9788-29bdd8017b10)
![image](https://github.com/user-attachments/assets/88b67128-1800-4c71-b395-f14d8574a95b)
![image](https://github.com/user-attachments/assets/5ff2c741-4036-43b6-99c4-44a9183f69f1)
![image](https://github.com/user-attachments/assets/c9479b66-b0e5-41f2-a713-d3bdba6691ba)
![image](https://github.com/user-attachments/assets/14f825dc-41e3-4fb9-b865-ab20fb7f9986)









