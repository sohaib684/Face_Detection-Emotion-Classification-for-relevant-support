import cv2
import mtcnn
#import numpy as np
#from pprint import pprint
import itertools
import math

#img = cv2.imread("image.jpg")


def get_landmarks(img):
    detector = mtcnn.MTCNN()
    results = detector.detect_faces(img)

    if not results:
        print("No faces detected.")

    if len(results) == 0:
        return None

    return results[0]["keypoints"]


def show_landmarks(img, landmarks):
    cv2.circle(img, landmarks["left_eye"], 2, (0, 255, 0), 2)
    cv2.circle(img, landmarks["right_eye"], 2, (0, 255, 0), 2)
    cv2.circle(img, landmarks["nose"], 2, (0, 255, 0), 2)
    cv2.circle(img, landmarks["mouth_left"], 2, (0, 255, 0), 2)
    cv2.circle(img, landmarks["mouth_right"], 2, (0, 255, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_distance(point1, point2):
    x1 = point1[0]
    y1 = point1[0]
    x2 = point2[0]
    y2 = point2[0]
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance


def get_parameters(landmarks):
    array = list(landmarks.values())
    combinations = itertools.combinations(array, 2)
    distances = []
    for combination in combinations:
        pointA = combination[0]
        pointB = combination[1]
        distance = find_distance(pointA, pointB)
        print(f"{pointA} - {pointB} : {distance}")
        distances.append(distance)
    return distances

# Main Function
def get_parameters_from_image(img):
    landmarks = get_landmarks(img)
    parameters = get_parameters(landmarks)
    return parameters
