import math
import subprocess
import sys

import numpy as np
import mediapipe as mp
import os
import OSCheck
import cv2
from pythonosc import udp_client
import Reset
from datetime import datetime, timedelta

print("Starting DanceMenuMovement.py")
client = udp_client.SimpleUDPClient("127.0.0.1", 6969)

def buildMessage(result):
    msg = result
    return msg
danceID = 0
nodCount = 0
nose1 = 0
y_move = 0
firstFrame = False
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle



cap = cv2.VideoCapture(0)
# Getting the width and height of the video
width = cap.get(3)
height = cap.get(4)
# Function will run for 5 secs
end_time = datetime.now() + timedelta(seconds=60)
selected = False
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while datetime.now() < end_time:

        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            # nose1 = landmarks[mp_pose.PoseLandmark.NOSE.value].y * height
            # Settings and initialising landmarks to be calculated / taken in
            # Could be written as functions using for sequences of dance moves

            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]

            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            left_kneeAngle = calculate_angle(left_hip, left_knee, left_ankle)
            right_kneeAngle = calculate_angle(right_hip, right_knee, right_ankle)
            if firstFrame == False:
                # nose0 = landmarks[mp_pose.PoseLandmark.NOSE.value].y
                firstFrame = True

            nose0 = landmarks[mp_pose.PoseLandmark.NOSE.value].y * height

            # nose2 = [landmarks[mp_pose.PoseLandmark.NOSE.value].y]

            # Calculating angles and storing them to be processed

            tpose_left = calculate_angle(left_hip, left_shoulder, left_elbow)
            tpose_right = calculate_angle(right_hip, right_shoulder, right_elbow)

            # Setting and displaying properties for angles to be displayed on screen

            # Pose Recognition Logic
            y_move += abs(nose1 - nose0)
            nose1 = nose0
            if (80 < left_kneeAngle < 150) and (80 < right_kneeAngle < 150):
                gesture = "T-POSE"
                print(gesture)
                client.send_message("/DanceMenu", buildMessage("T-POSE"))#can delete build message
                selected = True
                if selected:
                    break
                danceID = math.abs(danceID) % 3

                sys.exit()
            elif (80 < tpose_left < 110):
                gesture = "LEFT"
                print(gesture)
                danceID = (danceID - 1)
                client.send_message("/DanceMenu", buildMessage("LEFT"))#can delete build message
                #break
            elif (80 < tpose_right < 110):
                gesture = "RIGHT"
                print(gesture)

                danceID = (danceID + 1)
                client.send_message("/DanceMenu", buildMessage("RIGHT"))#can delete build message
                #break
        except:
            pass

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
if selected:
    OSCheck.checkOS("DanceScene",str(danceID))
if not selected:
    Reset.reset()

