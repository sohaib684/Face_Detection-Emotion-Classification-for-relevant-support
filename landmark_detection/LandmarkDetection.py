import cv2
import mtcnn
import numpy as np

<<<<<<< Updated upstream:landmark_detection/LandmarkDetection.py
path = "C:\College Works\Projects\CU_BTECH_PROJECT\datasets\face detection\images\2003\01\01\big\img_82.jpg"


# Load image
img = cv2.imread()

# Create MTCNN detector
detector = mtcnn.MTCNN()

# Detect faces and landmarks
results = detector.detect_faces(img)

# Extract landmarks for the first face (assuming there is at least one face in the image)
landmarks = results[0]["keypoints"]

# Extract coordinates for each landmark
left_eye = landmarks["left_eye"]
right_eye = landmarks["right_eye"]
nose = landmarks["nose"]
mouth_left = landmarks["mouth_left"]
mouth_right = landmarks["mouth_right"]

# Calculate transformation matrix for face alignment
eyes_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
dx = right_eye[0] - left_eye[0]
dy = right_eye[1] - left_eye[1]
angle = np.degrees(np.arctan2(dy, dx)) - 90
scale = 1
M = cv2.getRotationMatrix2D(eyes_center, angle, scale)

# Apply transformation matrix to image
aligned_face = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_CUBIC)

# Display aligned face and landmarks
cv2.imshow("Aligned Face", aligned_face)
cv2.circle(img, left_eye, 2, (0, 255, 0), 2)
cv2.circle(img, right_eye, 2, (0, 255, 0), 2)
cv2.circle(img, nose, 2, (0, 255, 0), 2)
cv2.circle(img, mouth_left, 2, (0, 255, 0), 2)
cv2.circle(img, mouth_right, 2, (0, 255, 0), 2)
cv2.imshow("Landmarks", img)
cv2.waitKey(0)
# cv2.destroyAllWindows()
=======
def align_face(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Create MTCNN detector
    detector = mtcnn.MTCNN()

    # Detect faces and landmarks
    results = detector.detect_faces(img)

    if len(results) == 0:
        print("No faces detected in the image.")
        return None

    # Extract landmarks for the first face
    landmarks = results[0]["keypoints"]

    print(landmarks)
    #print(hello)
    # # Extract coordinates for each landmark
    # left_eye = landmarks["left_eye"]
    # right_eye = landmarks["right_eye"]
    # nose = landmarks["nose"]
    # mouth_left = landmarks["mouth_left"]
    # mouth_right = landmarks["mouth_right"]

    # # Calculate transformation matrix for face alignment
    # eyes_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
    # dx = right_eye[0] - left_eye[0]
    # dy = right_eye[1] - left_eye[1]
    # angle = np.degrees(np.arctan2(dy, dx)) - 90
    # scale = 1
    # M = cv2.getRotationMatrix2D(eyes_center, angle, scale)

    # # Apply transformation matrix to image
    # aligned_face = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_CUBIC)

    # # Display aligned face and landmarks
    # cv2.imshow("Aligned Face", aligned_face)
    # cv2.circle(img, left_eye, 2, (0, 255, 0), 2)
    # cv2.circle(img, right_eye, 2, (0, 255, 0), 2)
    # cv2.circle(img, nose, 2, (0, 255, 0), 2)
    # cv2.circle(img, mouth_left, 2, (0, 255, 0), 2)
    # cv2.circle(img, mouth_right, 2, (0, 255, 0), 2)
    # cv2.imshow("Landmarks", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
>>>>>>> Stashed changes:landmark detection/LandmarkDetection.py
