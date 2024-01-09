import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)

#video feed
cap = cv2.VideoCapture(0)

def calculate_angle(a,b,c):
    a= np.array(a)
    b= np.array(b)
    c= np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0],b[0])-np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(180.0*radians/np.pi)

    if angle>180.0:
        angle= 360-angle
    return angle


while cap.isOpened():
    ret,frame = cap.read()


    # here the frame was captured by open cv and it will represent it in BGR format, but mediapipe analyses the image in RGB so,
    #color change
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    image.flags.writeable=False

    # feed the changed color image to a     

    results = pose.process(image)
    image.flags.writeable=True

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  

    try:
        landmarks = results.pose_landmarks.landmark

        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z]

        angle = calculate_angle(shoulder,elbow,wrist)
        


    except:
        pass


    mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)


    cv2.imshow('feed',image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
