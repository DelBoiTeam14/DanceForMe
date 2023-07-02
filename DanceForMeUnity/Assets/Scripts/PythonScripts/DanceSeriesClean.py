import os

import cv2
import numpy as np
import mediapipe as mp
import time
from Ballet import *
from Robo import *
from Cowboy import *
import sys
from pythonosc import udp_client
offset = 0
time.sleep(3)
# Importing All Necessary Libraries and Functions
danceID = "0"  # sys.argv[1]

cap = cv2.VideoCapture(0)
# Getting the width and height of the video
width = cap.get(3)
height = cap.get(4)
start = time.time()
checkStartTime = False
print("DANCEID: ", danceID)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
gesturePosInArray = 0

client = udp_client.SimpleUDPClient("127.0.0.1", 6969)


# Initializing Functions for pose drawing and Detection

def buildMessage(result):
    msg = result
    return msg


def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


# Initializing poses as functions to be passed into the array

#
# def TPose_Cal(tl, tr):
#     # Pose Recognition Logic
#     if (80 < tl < 110) and (80 < tr < 110):
#         gesture = "T-Pose"
#         return gesture
#     else:
#         gesture = "No pose"
#         return gesture
#
#
# def downPose(dl, dr):
#     if (0 < dl < 100) and (0 < dr < 100):
#         gesture = "Down Look"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def leftPose(ll, rl):
#     if (70 < ll < 120) and (80 < rl < 120):
#         gesture = "Left Pose"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def rightPose(rl, rr):
#     if (70 < rl < 120) and (80 < rr < 120):
#         gesture = "Right Pose"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def straightlineArms(la, ra):
#     if (160 < la < 200) and (160 < ra < 200):
#         gesture = "Arms Straight"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def leftL(la, ra):
#     if (70 < la < 120) and (-70 < ra < -120):
#         gesture = "Left L"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def rightL(la, ra):
#     if (70 < la < 120) and (70 < ra < 120):
#         gesture = "Right L"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def downStraight(lh, rh, la, ra):
#     if (160 < la < 200) and (160 < ra < 200):
#         if (130 < lh < 170) and (130 < rh < 170):
#             gesture = "Down Straight"
#             return gesture
#     else:
#         gesture = "No Pose"
#         return gesture
#
#
# def CowBoy(lh):
#     if (70 < lh < 110):
#         gesture = "CowBoy"
#         return gesture
#     else:
#         gesture = "No Pose"
#         return gesture


# Calculate Angles Functions for pose detection using angle heuristic implementation
bestScore = 0
checked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0]
scoreArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0]

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():

        ret, frame = cap.read()

        # Takes in the video input to convert to BGR to RGB for processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # results stored after being processed
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        try:
            landmarks = results.pose_landmarks.landmark

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

            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            left_hand = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]
            right_hand = [landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y]

            # Calculating angles and storing them to be processed

            print(" POINMT 1")

            tpose_left = calculate_angle(left_hip, left_shoulder, left_elbow)
            tpose_right = calculate_angle(right_hip, right_shoulder, right_elbow)

            left_armsAngle = calculate_angle(left_shoulder, left_elbow, left_wrist)
            right_armsAngle = calculate_angle(right_shoulder, right_elbow, right_wrist)

            left_hipsAngle = calculate_angle(left_shoulder, left_hip, left_knee)
            right_hipsAngle = calculate_angle(right_shoulder, right_hip, right_knee)

            left_shoulderAngle = calculate_angle(left_elbow, left_shoulder, left_hip)
            right_shoulderAngle = calculate_angle(right_elbow, right_shoulder, right_hip)

            left_kneeAngle = calculate_angle(left_hip, left_knee, left_ankle)
            right_kneeAngle = calculate_angle(right_hip, right_knee, right_ankle)

            left_handZ = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z]
            right_handZ = [landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z]
            nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x, landmarks[mp_pose.PoseLandmark.NOSE.value].y]

            # Setting and displaying properties for angles to be displayed on screen

            # cv2.putText(image, str(tpose_left),
            #             tuple(np.multiply(left_shoulder, [640, 480]).astype(int)),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            #
            # cv2.putText(image, str(tpose_right),
            #             tuple(np.multiply(right_shoulder, [640, 480]).astype(int)),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # Pose Recognition Logic
            # y_move += abs(nose1 - nose0)
            # if (80 < tpose_left < 110) and (80 < tpose_right < 110):
            #     gesture = "T-Pose"
            #     print(gesture)
            # # elif checksNod():         #This is implemented using nodding pigeon
            # #     gesture = "NOD"
            # #     print(gesture)
            # elif firstFrame and y_move >= 175:
            #     gesture = "NOD"
            #     y_move = 0
            #     print(gesture)
            # elif jumpTest(landmarks):
            #     gesture = "JUMP"
            #     print(gesture)
            # else:
            #     gesture = ""
            #     print(gesture)
            # nose1 = nose0

            # Dance Sequence

            # Dance move sequence

            # Could this be in its own file and be called in?

            # print(danceID == "3")
            if danceID == "0":
                print("Dance 0")
                gestureArray = [balletpose1(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose3(right_shoulderAngle, right_hipsAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose4(left_shoulderAngle, left_hipsAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose6(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle),
                                balletpose7(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle,
                                            left_kneeAngle),
                                balletpose8(left_shoulderAngle, right_shoulderAngle, left_hipsAngle),
                                balletpose9(left_shoulderAngle, right_shoulderAngle, right_hipsAngle),
                                balletpose8(left_shoulderAngle, right_shoulderAngle, left_hipsAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose6(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose6(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle),
                                balletpose2(left_kneeAngle, right_kneeAngle),
                                balletpose8(left_shoulderAngle, right_shoulderAngle, left_hipsAngle),
                                balletpose9(left_shoulderAngle, right_shoulderAngle, left_hipsAngle),
                                balletpose10(left_shoulderAngle, right_shoulderAngle),
                                balletpose11(left_shoulderAngle, right_shoulderAngle)
                                ]

                print("Point 2")

                if not checkStartTime:
                    start = time.time()
                    checkStartTime = True
                # gesture = gestureArray[gesturePosInArray]
                end = time.time()
                # print("hi")
                # print(end - start)
                # bestScore = 0
                # score = -1
                print(checked)
                if 4+offset < end - start < 5+offset:
                    score = gestureArray[0]
                    # print(score)
                    if scoreArray[0] < score:
                        scoreArray[0] = score

                    print("Pose 0 ", score)
                elif end - start < 6.51+offset:
                    if checked[0] == 0 :
                        client.send_message("/UserDetected", buildMessage(scoreArray[0]))
                        checked[0] = 1
                    score = gestureArray[1]
                    print(score)
                    if scoreArray[1] < score:
                        scoreArray[1] = score
                    print("Pose 1 ", score)
                elif end - start < (9+offset):
                    if checked[1] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[1]))
                        checked[1] = 1
                    score = gestureArray[2]
                    if scoreArray[2] < score:
                        scoreArray[2] = score
                    print("Pose 2 ", score)
                elif end - start < (12+offset):
                    if checked[2] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[2]))
                        checked[2] = 1
                    score = gestureArray[3]
                    if scoreArray[3] < score:
                        scoreArray[3] = score
                    print("Pose 3 ", score)
                elif end - start < (13.6+offset):
                    if checked[3] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[3]))
                        checked[3] = 1
                    score = gestureArray[4]
                    if scoreArray[4] < score:
                        scoreArray[4] = score
                    print("Pose 4 ", score)
                elif end - start < (16+offset):
                    if checked[4] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[4]))
                        checked[4] = 1
                    score = gestureArray[5]
                    if scoreArray[5] < score:
                        scoreArray[5] = score
                    print("Pose 5 ", score)
                elif end - start < (15.91+offset): #pose1
                    if checked[5] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[5]))
                        checked[5] = 1
                    score = gestureArray[6]
                    if scoreArray[6] < score:
                        scoreArray[6] = score
                    print("Pose 6 ", score)
                elif end - start < (18.57+offset):  # -> no score
                    print(" ")
                elif end - start < (19+offset):
                    if checked[6] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[6]))
                        checked[6] = 1
                    score = gestureArray[7]
                    if scoreArray[7] < score:
                        scoreArray[7] = score
                    print("Pose 7 ", score)
                elif end - start < (21+offset):
                    if checked[7] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[7]))
                        checked[7] = 1
                    score = gestureArray[8]
                    if scoreArray[8] < score:
                        scoreArray[8] = score
                    print("Pose 8 ", score)
                elif end - start < (25+offset):
                    if checked[8] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[8]))
                        checked[8] = 1
                    score = gestureArray[9]
                    if scoreArray[9] < score:
                        scoreArray[9] = score
                    print("Pose 9 ", score)
                elif end - start < (27+offset):
                    if checked[9] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[9]))
                        checked[9] = 1
                    score = gestureArray[10]
                    if scoreArray[10] < score:
                        scoreArray[10] = score
                    print("Pose 10 ", score)
                elif end - start < (29+offset):
                    if checked[10] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[10]))
                        checked[10] = 1
                    score = gestureArray[11]
                    if scoreArray[11] < score:
                        scoreArray[11] = score
                    print("Pose 11 ", score)
                elif end - start < (31.5+offset):
                    if checked[11] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[11]))
                        checked[11] = 1
                    score = gestureArray[12]
                    if scoreArray[12] < score:
                        scoreArray[12] = score
                    print("Pose 12 ", score)
                elif end - start < (33+offset):
                    if checked[12] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[12]))
                        checked[12] = 1
                    score = gestureArray[13]
                    if scoreArray[13] < score:
                        scoreArray[13] = score
                    print("Pose 13 ", score)
                elif end - start < (35+offset):
                    if checked[13] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[13]))
                        checked[13] = 1
                    score = gestureArray[14]
                    if scoreArray[14] < score:
                        scoreArray[14] = score
                        print("Pose 14 ", score)
                elif end - start < (36+offset):
                    if checked[14] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[14]))
                        checked[14] = 1
                    score = gestureArray[15]
                    if scoreArray[15] < score:
                        scoreArray[15] = score
                    print("Pose 15 ", score)
                elif end - start < (38+offset):
                    if checked[15] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[15]))
                        checked[15] = 1
                    score = gestureArray[16]
                    if scoreArray[16] < score:
                        scoreArray[16] = score
                    print("Pose 16 ", score)
                elif end - start < (39.5+offset):
                    if checked[16] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[16]))
                        checked[16] = 1
                    score = gestureArray[17]
                    if scoreArray[17] < score:
                        scoreArray[17] = score
                    print("Pose 17 ", score)
                elif end - start < (41.5+offset):
                    if checked[17] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[17]))
                        checked[17] = 1
                    score = gestureArray[18]
                    if scoreArray[18] < score:
                        scoreArray[18] = score
                    print("Pose 18 ", score)
                elif end - start < (44+offset):
                    print(" ")
                elif end - start < (50.5+offset):
                    if checked[18] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[18]))
                        checked[18] = 1
                    score = gestureArray[19]
                    if scoreArray[19] < score:
                        scoreArray[19] = score
                    print("Pose 19 ", score)
                elif end - start < (53+offset):
                    if checked[19] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[19]))
                        checked[19] = 1
                    score = gestureArray[20]
                    if scoreArray[20] < score:
                        scoreArray[20] = score
                    print("Pose 20 ", score)
                # elif end - start < (49.42):
                #     if checked[20] == 0:
                #         client.send_message("/UserDetected", buildMessage(scoreArray[20]))
                #         checked[20] = 1
                #     score = gestureArray[21]
                #     if scoreArray[21] < score:
                #         scoreArray[21] = score
                #     print("Pose 21 ", score)
                else:
                    if checked[21] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[20]))
                        checked[21] = 1
                    # print("END")
                    print(scoreArray, "\n")
                    break

            elif danceID == "1":
                gestureArray4 = [cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 #cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
                                 cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
                                 cowpose5(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle,
                                          left_kneeAngle),
                                 cowpose6(left_armsAngle, right_armsAngle),
                                 cowpose5(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle,
                                          left_kneeAngle),
                                 cowpose6(left_armsAngle, right_armsAngle),
                                 cowpose7(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle,
                                          right_kneeAngle),
                                 cowpose6(left_armsAngle, right_armsAngle),
                                 cowpose7(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle,
                                          right_kneeAngle),
                                 cowpose6(left_armsAngle, right_armsAngle),
                                 cowpose8(right_armsAngle, right_hand, nose),
                                 cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                          right_kneeAngle),
                                 cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                          right_kneeAngle),
                                 cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                          right_kneeAngle),
                                 cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                          right_kneeAngle),
                                 cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose11(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose11(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           left_kneeAngle),
                                 cowpose12(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           right_kneeAngle),
                                 cowpose12(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle,
                                           right_kneeAngle),
                                 cowpose13(left_shoulderAngle, right_shoulderAngle),
                                 cowpose14(left_handZ, right_handZ),
                                 cowpose15(left_handZ, right_handZ),
                                 cowpose14(left_handZ, right_handZ),
                                 cowpose15(left_handZ, right_handZ),
                                 cowpose6(left_armsAngle, right_armsAngle),  # shovel up similar to pistol hold
                                 ]
                if not checkStartTime:
                    start = time.time()
                    checkStartTime = True
                # gesture = gestureArray[gesturePosInArray]
                end = time.time()
                # print("hi")
                # print(end - start)
                # bestScore = 0
                # score = -1
                print(checked)
                if 5.1+offset < end - start < 8.54+offset:
                    score = gestureArray[0]
                    # print(score)
                    if scoreArray[0] < score:
                        scoreArray[0] = score

                    print("Pose 0 ", score)
                elif end - start < 9.32+offset:
                    if checked[0] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[0]))
                        checked[0] = 1
                    score = gestureArray[1]
                    print(score)
                    if scoreArray[1] < score:
                        scoreArray[1] = score
                    print("Pose 1 ", score)
                elif end - start < (10.5+offset):
                    if checked[1] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[1]))
                        checked[1] = 1
                    score = gestureArray[2]
                    if scoreArray[2] < score:
                        scoreArray[2] = score
                    print("Pose 2 ", score)
                elif end - start < (11.25+offset):
                    if checked[2] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[2]))
                        checked[2] = 1
                    score = gestureArray[3]
                    if scoreArray[3] < score:
                        scoreArray[3] = score
                    print("Pose 3 ", score)
                elif end - start < (12.18+offset):
                    if checked[3] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[3]))
                        checked[3] = 1
                    score = gestureArray[4]
                    if scoreArray[4] < score:
                        scoreArray[4] = score
                    print("Pose 4 ", score)
                elif end - start < (13+offset):
                    if checked[4] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[4]))
                        checked[4] = 1
                    score = gestureArray[5]
                    if scoreArray[5] < score:
                        scoreArray[5] = score
                    print("Pose 5 ", score)
                elif end - start < (14.68+offset):
                    if checked[5] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[5]))
                        checked[5] = 1
                    score = gestureArray[6]
                    if scoreArray[6] < score:
                        scoreArray[6] = score
                    print("Pose 6 ", score)
                elif end - start < (15.68+offset):
                    if checked[6] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[6]))
                        checked[6] = 1
                    score = gestureArray[7]
                    if scoreArray[7] < score:
                        scoreArray[7] = score
                    print("Pose 7 ", score)
                elif end - start < (16.5+offset):
                    if checked[7] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[7]))
                        checked[7] = 1
                    score = gestureArray[8]
                    if scoreArray[8] < score:
                        scoreArray[8] = score
                    print("Pose 8 ", score)
                elif end - start < (18.25+offset):
                    if checked[8] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[8]))
                        checked[8] = 1
                    score = gestureArray[9]
                    if scoreArray[9] < score:
                        scoreArray[9] = score
                    print("Pose 9 ", score)
                elif end - start < (19.2+offset):
                    if checked[9] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[9]))
                        checked[9] = 1
                    score = gestureArray[10]
                    if scoreArray[10] < score:
                        scoreArray[10] = score
                    print("Pose 10 ", score)
                elif end - start < (20.5+offset):
                    if checked[10] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[10]))
                        checked[10] = 1
                    score = gestureArray[11]
                    if scoreArray[11] < score:
                        scoreArray[11] = score
                    print("Pose 11 ", score)
                elif end - start < (21.8+offset):
                    if checked[11] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[11]))
                        checked[11] = 1
                    score = gestureArray[12]
                    if scoreArray[12] < score:
                        scoreArray[12] = score
                    print("Pose 12 ", score)
                elif end - start < (22.5+offset):
                    if checked[12] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[12]))
                        checked[12] = 1
                    score = gestureArray[13]
                    if scoreArray[13] < score:
                        scoreArray[13] = score
                    print("Pose 13 ", score)
                elif end - start < (23.35+offset):
                    if checked[13] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[13]))
                        checked[13] = 1
                    score = gestureArray[14]
                    if scoreArray[14] < score:
                        scoreArray[14] = score
                        print("Pose 14 ", score)
                elif end - start < (24.5+offset):
                    if checked[14] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[14]))
                        checked[14] = 1
                    score = gestureArray[15]
                    if scoreArray[15] < score:
                        scoreArray[15] = score
                    print("Pose 15 ", score)
                elif end - start < (25.03+offset):
                    if checked[15] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[15]))
                        checked[15] = 1
                    score = gestureArray[16]
                    if scoreArray[16] < score:
                        scoreArray[16] = score
                    print("Pose 16 ", score)
                elif end - start < (26+offset):
                    if checked[16] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[16]))
                        checked[16] = 1
                    score = gestureArray[17]
                    if scoreArray[17] < score:
                        scoreArray[17] = score
                    print("Pose 17 ", score)
                elif end - start < (26.8+offset):
                    if checked[17] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[17]))
                        checked[17] = 1
                    score = gestureArray[18]
                    if scoreArray[18] < score:
                        scoreArray[18] = score
                    print("Pose 18 ", score)
                elif end - start < (28.3+offset):
                    if checked[18] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[18]))
                        checked[18] = 1
                    score = gestureArray[19]
                    if scoreArray[19] < score:
                        scoreArray[19] = score
                    print("Pose 19 ", score)
                elif end - start < (33+offset):
                    if checked[19] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[19]))
                        checked[19] = 1
                    score = gestureArray[20]
                    if scoreArray[20] < score:
                        scoreArray[20] = score
                    print("Pose 20 ", score)
                elif end - start < (34+offset):
                    if checked[20] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[20]))
                        checked[20] = 1
                    score = gestureArray[21]
                    if scoreArray[21] < score:
                        scoreArray[21] = score
                    print("Pose 21 ", score)
                elif end - start < (35+offset):
                    if checked[21] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[21]))
                        checked[21] = 1
                    score = gestureArray[22]
                    if scoreArray[22] < score:
                        scoreArray[22] = score
                    print("Pose 22 ", score)
                elif end - start < (36+offset):
                    if checked[22] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[22]))
                        checked[22] = 1
                    score = gestureArray[23]
                    if scoreArray[23] < score:
                        scoreArray[23] = score
                    print("Pose 23 ", score)
                elif end - start < (37.3+offset):
                    if checked[23] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[23]))
                        checked[23] = 1
                    score = gestureArray[23]
                    if scoreArray[24] < score:
                        scoreArray[24] = score
                    print("Pose 24 ", score)
                elif end - start < (38.1+offset):
                    if checked[24] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[24]))
                        checked[24] = 1
                    score = gestureArray[23]
                    if scoreArray[25] < score:
                        scoreArray[25] = score
                    print("Pose 25 ", score)
                elif end - start < (39+offset):
                    if checked[25] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[25]))
                        checked[25] = 1
                    score = gestureArray[23]
                    if scoreArray[26] < score:
                        scoreArray[26] = score
                    print("Pose 26 ", score)
                elif end - start < (40+offset):
                    if checked[26] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[26]))
                        checked[26] = 1
                    score = gestureArray[23]
                    if scoreArray[27] < score:
                        scoreArray[27] = score
                    print("Pose 27 ", score)
                elif end - start < (40.7+offset):
                    if checked[27] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[27]))
                        checked[27] = 1
                    score = gestureArray[23]
                    if scoreArray[28] < score:
                        scoreArray[28] = score
                    print("Pose 28 ", score)
                elif end - start < (41.66+offset):
                    if checked[28] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[28]))
                        checked[28] = 1
                    score = gestureArray[23]
                    if scoreArray[29] < score:
                        scoreArray[29] = score
                    print("Pose 29 ", score)
                elif end - start < (42.5+offset):
                    if checked[29] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[29]))
                        checked[29] = 1
                    score = gestureArray[23]
                    if scoreArray[30] < score:
                        scoreArray[30] = score
                    print("Pose 30 ", score)
                elif end - start < (43.5+offset):
                    if checked[30] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[30]))
                        checked[30] = 1
                    score = gestureArray[23]
                    if scoreArray[31] < score:
                        scoreArray[31] = score
                    print("Pose 31 ", score)
                elif end - start < (44.5+offset):
                    if checked[31] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[31]))
                        checked[31] = 1
                    score = gestureArray[23]
                    if scoreArray[32] < score:
                        scoreArray[32] = score
                    print("Pose 32 ", score)
                elif end - start < (46.8+offset):
                    if checked[32] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[32]))
                        checked[32] = 1
                    score = gestureArray[23]
                    if scoreArray[33] < score:
                        scoreArray[33] = score
                    print("Pose 33 ", score)
                elif end - start < (48+offset):
                    if checked[33] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[33]))
                        checked[33] = 1
                    score = gestureArray[23]
                    if scoreArray[34] < score:
                        scoreArray[34] = score
                    print("Pose 34 ", score)
                elif end - start < (49+offset):
                    if checked[34] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[34]))
                        checked[34] = 1
                    score = gestureArray[23]
                    if scoreArray[35] < score:
                        scoreArray[35] = score
                    print("Pose 35 ", score)
                elif end - start < (52+offset):
                    if checked[35] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[35]))
                        checked[35] = 1
                    score = gestureArray[23]
                    if scoreArray[36] < score:
                        scoreArray[36] = score
                    print("Pose 36 ", score)
                elif end - start < (54+offset):
                    if checked[36] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[36]))
                        checked[36] = 1
                    score = gestureArray[23]
                    if scoreArray[37] < score:
                        scoreArray[37] = score
                    print("Pose 37 ", score)
                elif end - start < (56.5+offset):
                    if checked[37] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[37]))
                        checked[37] = 1
                    score = gestureArray[23]
                    if scoreArray[38] < score:
                        scoreArray[38] = score
                    print("Pose 38 ", score)
                # elif end - start < (28.91 + 2.83 + 5):
                #     if checked[38] == 0:
                #         client.send_message("/UserDetected", buildMessage(scoreArray[22]))
                #         checked[38] = 1
                #     score = gestureArray[23]
                #     if scoreArray[39] < score:
                #         scoreArray[39] = score
                #     print("Pose 39 ", score)
                else:
                    if checked[38] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[38]))
                        checked[38] = 1
                    # print("END")
                    print(scoreArray, "\n")
            elif danceID == "2":
                gestureArray = [pose1(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose2(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose3(right_armsAngle, right_kneeAngle),
                                pose4(left_armsAngle, left_kneeAngle),
                                pose5(left_kneeAngle, right_kneeAngle, right_armsAngle,
                                      left_armsAngle),
                                pose6(left_kneeAngle, right_kneeAngle, right_armsAngle,
                                      left_armsAngle),
                                pose7(right_shoulderAngle, left_shoulderAngle, right_armsAngle, left_armsAngle),
                                pose8(right_shoulderAngle, left_shoulderAngle, right_armsAngle, left_armsAngle),
                                pose10(left_armsAngle, left_shoulderAngle, right_shoulderAngle, right_armsAngle),
                                pose11(left_armsAngle, left_shoulderAngle, right_shoulderAngle, right_armsAngle),
                                pose10(left_armsAngle, left_shoulderAngle, right_shoulderAngle, right_armsAngle),
                                pose11(left_armsAngle, left_shoulderAngle, right_shoulderAngle, right_armsAngle),

                                pose21(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose22(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose23(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose24(right_armsAngle, right_shoulderAngle, left_armsAngle, left_shoulderAngle),
                                pose25(right_kneeAngle, right_armsAngle, left_armsAngle, left_shoulderAngle),
                                pose26(left_kneeAngle, left_armsAngle, right_armsAngle, right_shoulderAngle),
                                pose27(right_kneeAngle, right_armsAngle, left_armsAngle, left_hipsAngle),
                                pose28(right_kneeAngle, right_armsAngle, left_armsAngle, left_hipsAngle,
                                       left_shoulderAngle),
                                pose29(right_hand[0], right_hand[1], right_hip[0], right_hip[1], left_hip[0],
                                       left_hip[1],
                                       left_elbow[0], left_elbow[1]),
                                pose210(left_hand[0], left_hand[1], right_hip[0], right_hip[1], left_hip[0],
                                        left_hip[1],
                                        right_elbow[0], right_elbow[1]),
                                pose211(left_hand[1], right_hand[1], landmarks[mp_pose.PoseLandmark.NOSE.value].y)]

                # gestureArray = gestureArray3
                if not checkStartTime:
                    start = time.time()
                    checkStartTime = True
                # gesture = gestureArray[gesturePosInArray]
                end = time.time()
                # print("hi")
                # print(end - start)
                # bestScore = 0
                # score = -1
                print(checked)
                if 3 < end - start < 4.5+offset:
                    score = gestureArray[0]
                    # print(score)
                    if scoreArray[0] < score:
                        scoreArray[0] = score

                    print("Pose 0 ", score)
                elif end - start < 5.5 + offset:
                    if checked[0] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[0]))
                        checked[0] = 1
                    score = gestureArray[1]
                    print(score)
                    if scoreArray[1] < score:
                        scoreArray[1] = score
                    print("Pose 1 ", score)
                elif end - start < (6.65+offset):
                    if checked[1] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[1]))
                        checked[1] = 1
                    score = gestureArray[2]
                    if scoreArray[2] < score:
                        scoreArray[2] = score
                    print("Pose 2 ", score)
                elif end - start < (8+offset):
                    if checked[2] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[2]))
                        checked[2] = 1
                    score = gestureArray[3]
                    if scoreArray[3] < score:
                        scoreArray[3] = score
                    print("Pose 3 ", score)
                elif end - start < (10.5+offset):
                    if checked[3] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[3]))
                        checked[3] = 1
                    score = gestureArray[4]
                    if scoreArray[4] < score:
                        scoreArray[4] = score
                    print("Pose 4 ", score)
                elif end - start < (12.5+offset):
                    if checked[4] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[4]))
                        checked[4] = 1
                    score = gestureArray[5]
                    if scoreArray[5] < score:
                        scoreArray[5] = score
                    print("Pose 5 ", score)
                elif end - start < (14.35+ offset):
                    if checked[5] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[5]))
                        checked[5] = 1
                    score = gestureArray[6]
                    if scoreArray[6] < score:
                        scoreArray[6] = score
                    print("Pose 6 ", score)
                elif end - start < (16.70+offset):
                    if checked[6] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[6]))
                        checked[6] = 1
                    score = gestureArray[7]
                    if scoreArray[7] < score:
                        scoreArray[7] = score
                    print("Pose 7 ", score)
                elif end - start < (17.75 + offset):
                    if checked[7] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[7]))
                        checked[7] = 1
                    score = gestureArray[8]
                    if scoreArray[8] < score:
                        scoreArray[8] = score
                    print("Pose 8 ", score)
                elif end - start < (18.65 + offset ):
                    if checked[8] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[8]))
                        checked[8] = 1
                    score = gestureArray[9]
                    if scoreArray[9] < score:
                        scoreArray[9] = score
                    print("Pose 9 ", score)
                elif end - start < (20 + offset):
                    if checked[9] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[9]))
                        checked[9] = 1
                    score = gestureArray[10]
                    if scoreArray[10] < score:
                        scoreArray[10] = score
                    print("Pose 10 ", score)
                elif end - start < (23 + offset):
                    if checked[10] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[10]))
                        checked[10] = 1
                    score = gestureArray[11]
                    if scoreArray[11] < score:
                        scoreArray[11] = score
                    print("Pose 11 ", score)
                elif end - start < (24 + offset):
                    if checked[11] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[11]))
                        checked[11] = 1
                    score = gestureArray[12]
                    if scoreArray[12] < score:
                        scoreArray[12] = score
                    print("Pose 12 ", score)
                elif end - start < (25 + offset):
                    if checked[12] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[12]))
                        checked[12] = 1
                    score = gestureArray[13]
                    if scoreArray[13] < score:
                        scoreArray[13] = score
                    print("Pose 13 ", score)
                elif end - start < (26 + offset):
                    if checked[13] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[13]))
                        checked[13] = 1
                    score = gestureArray[14]
                    if scoreArray[14] < score:
                        scoreArray[14] = score
                        print("Pose 14 ", score)
                elif end - start < (26.7 + offset):
                    if checked[14] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[14]))
                        checked[14] = 1
                    score = gestureArray[15]
                    if scoreArray[15] < score:
                        scoreArray[15] = score
                    print("Pose 15 ", score)
                elif end - start < (27.65 +offset):
                    if checked[15] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[15]))
                        checked[15] = 1
                    score = gestureArray[16]
                    if scoreArray[16] < score:
                        scoreArray[16] = score
                    print("Pose 16 ", score)
                elif end - start < (29 +offset):
                    if checked[16] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[16]))
                        checked[16] = 1
                    score = gestureArray[17]
                    if scoreArray[17] < score:
                        scoreArray[17] = score
                    print("Pose 17 ", score)
                elif end - start < (31.4 +offset):
                    if checked[17] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[17]))
                        checked[17] = 1
                    score = gestureArray[18]
                    if scoreArray[18] < score:
                        scoreArray[18] = score
                    print("Pose 18 ", score)
                elif end - start < (32.1 +offset):
                    if checked[18] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[18]))
                        checked[18] = 1
                    score = gestureArray[19]
                    if scoreArray[19] < score:
                        scoreArray[19] = score
                    print("Pose 19 ", score)
                elif end - start < (33.1+offset):
                    if checked[19] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[19]))
                        checked[19] = 1
                    score = gestureArray[20]
                    if scoreArray[20] < score:
                        scoreArray[20] = score
                    print("Pose 20 ", score)
                elif end - start < (34.1+offset):
                    if checked[20] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[20]))
                        checked[20] = 1
                    score = gestureArray[21]
                    if scoreArray[21] < score:
                        scoreArray[21] = score
                    print("Pose 21 ", score)
                elif end - start < (35+offset):
                    if checked[21] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[21]))
                        checked[21] = 1
                    score = gestureArray[22]
                    if scoreArray[22] < score:
                        scoreArray[22] = score
                    print("Pose 22 ", score)
                elif end - start < (36.5+offset):
                    if checked[22] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[22]))
                        checked[22] = 1
                    score = gestureArray[23]
                    if scoreArray[23] < score:
                        scoreArray[23] = score
                    print("Pose 23 ", score)
                else:
                    if checked[23] == 0:
                        client.send_message("/UserDetected", buildMessage(scoreArray[23]))
                        checked[23] = 1
                    break
                    # print("END")
                    print(scoreArray, "\n")
                # if end - start < 1.67:
                #     score = gestureArray[0]
                #     # print(score)
                #     if scoreArray[0] < score:
                #         scoreArray[0] = score
                #     print("Pose 0 ", score)
                # elif end - start < 2.83:
                #     score = gestureArray[1]
                #     print(score)
                #     if scoreArray[1] < score:
                #         scoreArray[1] = score
                #     print("Pose 1 ", score)
                # elif end - start < (0.67 + 2.83):
                #     score = gestureArray[2]
                #     if scoreArray[2] < score:
                #         scoreArray[2] = score
                #     print("Pose 2 ", score)
                # elif end - start < (1.67 + 2.83):
                #     score = gestureArray[3]
                #     if scoreArray[3] < score:
                #         scoreArray[3] = score
                #     print("Pose 3 ", score)
                # elif end - start < (2.67 + 2.83):
                #     score = gestureArray[4]
                #     if scoreArray[4] < score:
                #         scoreArray[4] = score
                #     print("Pose 4 ", score)
                # elif end - start < (5.09 + 2.83):
                #     score = gestureArray[5]
                #     if scoreArray[5] < score:
                #         scoreArray[5] = score
                #     print("Pose 5 ", score)
                # elif end - start < (7.17 + 2.83):
                #     score = gestureArray[6]
                #     if scoreArray[6] < score:
                #         scoreArray[6] = score
                #     print("Pose 6 ", score)
                # elif end - start < (9.52 + 2.83):
                #     score = gestureArray[7]
                #     if scoreArray[7] < score:
                #         scoreArray[7] = score
                #     print("Pose 7 ", score)
                # elif end - start < (11.12 + 2.83):
                #     score = gestureArray[8]
                #     if scoreArray[8] < score:
                #         scoreArray[8] = score
                #     print("Pose 8 ", score)
                # elif end - start < (12.04 + 2.83):
                #     score = gestureArray[9]
                #     if scoreArray[9] < score:
                #         scoreArray[9] = score
                #     print("Pose 9 ", score)
                # elif end - start < (12.79 + 2.83):
                #     score = gestureArray[10]
                #     if scoreArray[10] < score:
                #         scoreArray[10] = score
                #     print("Pose 10 ", score)
                # elif end - start < (13.54 + 2.83):
                #     score = gestureArray[11]
                #     if scoreArray[11] < score:
                #         scoreArray[11] = score
                #     print("Pose 11 ", score)
                # elif end - start < (14.29 + 2.83):
                #     score = gestureArray[12]
                #     if scoreArray[12] < score:
                #         scoreArray[12] = score
                #     print("Pose 12 ", score)
                # elif end - start < (17.76 + 2.83):
                #     score = gestureArray[13]
                #     if scoreArray[13] < score:
                #         scoreArray[13] = score
                #     print("Pose 13 ", score)
                # elif end - start < (18.76 + 2.83):
                #     score = gestureArray[14]
                #     if scoreArray[14] < score:
                #         scoreArray[14] = score
                #         print("Pose 14 ", score)
                # elif end - start < (19.76 + 2.83):
                #     score = gestureArray[15]
                #     if scoreArray[15] < score:
                #         scoreArray[15] = score
                #     print("Pose 15 ", score)
                # elif end - start < (20.59 + 2.83):
                #     score = gestureArray[16]
                #     if scoreArray[16] < score:
                #         scoreArray[16] = score
                #     print("Pose 16 ", score)
                # elif end - start < (21.5 + 2.83):
                #     score = gestureArray[17]
                #     if scoreArray[17] < score:
                #         scoreArray[17] = score
                #     print("Pose 17 ", score)
                # elif end - start < (22.41 + 2.83):
                #     score = gestureArray[18]
                #     if scoreArray[18] < score:
                #         scoreArray[18] = score
                #     print("Pose 18 ", score)
                # elif end - start < (24.08 + 2.83):
                #     score = gestureArray[19]
                #     if scoreArray[19] < score:
                #         scoreArray[19] = score
                #     print("Pose 19 ", score)
                # elif end - start < (26.08 + 2.83):
                #     score = gestureArray[20]
                #     if scoreArray[20] < score:
                #         scoreArray[20] = score
                #     print("Pose 20 ", score)
                # elif end - start < (27.08 + 2.83):
                #     score = gestureArray[21]
                #     if scoreArray[21] < score:
                #         scoreArray[21] = score
                #     print("Pose 21 ", score)
                # elif end - start < (28.08 + 2.83):
                #     score = gestureArray[22]
                #     if scoreArray[22] < score:
                #         scoreArray[22] = score
                #     print("Pose 22 ", score)
                # elif end - start < (28.91 + 2.83):
                #     score = gestureArray[23]
                #     if scoreArray[23] < score:
                #         scoreArray[23] = score
                #     print("Pose 23 ", score)
                # else:
                #     # print("END")
                #     print(scoreArray, "\n")
                if score == 0:
                    score = 1
                # client.send_message("/UserDetected", buildMessage(score))
            end = time.time()
            # print(end - start)
            # gesture = gestureArray[1] #gesture is the output of the dance move

            # Rendering T-Pose Display
            # cv2.rectangle(image, (0, 0), (255, 73), (245, 117, 16), -1)
            #
            # cv2.putText(image, 'Pose: ', (15, 12),  # Starting Coord
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # # Font,                  Font Size, Color, Line Width, Line type
            # cv2.putText(image, str(gesture), (10, 60),  # replace str(gesture) with str(poses)
            #             cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
            #
            # # Render Time Count Down
            # cv2.rectangle(image, (260, 0), (510, 73), (245, 117, 16), -1)
            # cv2.putText(image, 'Time: ', (215, 12),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # cv2.putText(image, (end - start), (10, 60),
            #             cv2.FONT_HERSHEY_SIMPELX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Uncomment print(landmarks) to display angles on screen
            # print(landmarks)
        except:
            pass

        # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        #                           mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
        #                           mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
        #
        # cv2.imshow('Mediapipe Feed', image)

        # Title of window/video frame

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        # If key pressed programme is stopped

    cap.release()
    cv2.destroyAllWindows()

pid = 0
p = subprocess.Popen("tasklist /v /fi \"imagename eq cmd.exe\" /fo csv", stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.decode().splitlines():
    if "DanceScene.bat" in line:
        pid = int(line.split(",")[1].replace("\"", ""))
subprocess.call("taskkill /f /pid {} /t".format(pid), shell=True)
# TerminateUnityExe.bat will terminate the current DanceForMe.exe instance
sys.exit()
