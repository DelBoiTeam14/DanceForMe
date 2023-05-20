import cv2
import mediapipe as mp
import time
import UnityEngine as ue
import SendingCS as SCS
#DOWNLOAD DEPENDENCIES USING THE FOLLOWING COMMAND
# pip install -r requirements.txt
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Setting the built-in camera
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    # Keep activating while the camera is on
    while cap.isOpened():

            # success(bool) checks if the camera is working, image stores the image from cap.read()
            success, image = cap.read()

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            image.flags.writeable = False

            # Process the image by passing in the image
            results = pose.process(image)

            image.flags.writeable = True
        
            # results.pose_landmarks has four values:
            # X,Y,Z and visibility
            # If the user is not here
            # results.pose_landmarks will output none
            if results.pose_landmarks:
                SCS.sendingData("True")
                break



# Release the camera, outside of while loop
cap.release()
