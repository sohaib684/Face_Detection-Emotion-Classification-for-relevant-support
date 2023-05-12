from face_detection.FaceDetection import FaceDetection
import cv2

vid = cv2.VideoCapture(1)

faceDetection = FaceDetection()


while True:
    ret, frame = vid.read()

    ret, output = faceDetection.getFaceRect(frame)
    
    if (ret == 0):
        cv2.imshow("window", output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    print("running program")
  
vid.release()
cv2.destroyAllWindows()

"""image = cv2.imread("datasets/face detection/images/2002/07/19/big/img_422.jpg")
ret, frame = faceDetection.getFaceRect(image)
if (ret == 0):
    cv2.imshow("window", frame)
    cv2.waitKey(0)
    
else:
    print("error")
    
cv2.destroyAllWindows()"""