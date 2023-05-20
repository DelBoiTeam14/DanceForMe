import socket
import numpy as np
import mediapipe as mp
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
from pythonosc import udp_client



client = udp_client.SimpleUDPClient("127.0.0.1", 6969)

def buildMessage(result):
    msg = result
    return msg.upper()

def scorecalc(first,second, userscore): 
    midpoint = (second + first) / 2 
    distanceFromMidpoint = abs(userscore - midpoint)
    range_limit = abs(first - second) * 0.2 # within 20% is great

    if distanceFromMidpoint <= range_limit:
        return 200 #Score for great move
    elif distanceFromMidpoint <= range_limit * 3: # within 60% is good
        return 100 #Score for good move
    else: # okay
        return 50# Score for okay move


nodCount = 0
nose1 = 0
y_move = 0
firstFrame = False
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



# jumpTest() takes in a list of landmark. And if landmarkList[0].y (NOSE landmark) times 480 is less than 80
# That means the user in frame is jumping
# FIXME: Jumping and Nodding might be detected at the same time
def jumpTest(landmarkList):
    if (landmarkList[0].y * 480) < 80:
        return True
    return False


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
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():

        #vc.record()
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


            if firstFrame == False:
                # nose0 = landmarks[mp_pose.PoseLandmark.NOSE.value].y
                firstFrame = True

            nose0 = landmarks[mp_pose.PoseLandmark.NOSE.value].y * height

            # nose2 = [landmarks[mp_pose.PoseLandmark.NOSE.value].y]

            # Calculating angles and storing them to be processed

            tpose_left = calculate_angle(left_hip, left_shoulder, left_elbow)
            tpose_right = calculate_angle(right_hip, right_shoulder, right_elbow)

            # Setting and displaying properties for angles to be displayed on screen

            cv2.putText(image, str(tpose_left),
                        tuple(np.multiply(left_shoulder, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, str(tpose_right),
                        tuple(np.multiply(right_shoulder, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # Pose Recognition Logic
            y_move += abs(nose1 - nose0)
            nose1 = nose0
            if (80 < tpose_left < 110) and (80 < tpose_right < 110):
                gesture = "T-POSE"
                print(gesture)
                client.send_message("/UserDetected", buildMessage("T-POSE"))
                break
            elif firstFrame and y_move >= 175:
                nodCount += 1
                gesture = "NOD"
                y_move = 0
                print(gesture)
               # if nodCount == 2:
                client.send_message("/UserDetected", buildMessage("NOD"))
                #break
            elif jumpTest(landmarks):
                gesture = "JUMP"
                print(gesture)
                client.send_message("/UserDetected", buildMessage("JUMP"))
                #break
            elif (80 < tpose_left < 110):
                gesture = "LEFT"
                print(gesture)
                client.send_message("/UserDetected", buildMessage("LEFT"))
                #break
            elif (80 < tpose_right < 110):
                gesture = "RIGHT"
                print(gesture)
                client.send_message("/UserDetected", buildMessage("RIGHT"))
                #break
            else:
                gesture = ""
                client.send_message("/UserDetected", buildMessage(""))
                print(gesture)
                #break

            # Rendering T-Pose Display
            cv2.rectangle(image, (0, 0), (255, 73), (245, 117, 16), -1)

            cv2.putText(image, 'Pose: ', (15, 12),  # Starting Coord
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # FileNotFoundErrort,                  Font Size, Color, Line Width, Line type
            cv2.putText(image, str(gesture), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Uncomment print(landmarks) to display angles on screen
            # print(landmarks)
        except:
            pass

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))


        #cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

