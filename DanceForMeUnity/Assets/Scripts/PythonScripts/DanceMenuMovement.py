import math
import sys
import AngleCalculation
import mediapipe as mp
import OSCheck
import cv2
from pythonosc import udp_client
import Reset
from datetime import datetime, timedelta

print("Starting DanceMenuMovement.py")
client = udp_client.SimpleUDPClient("127.0.0.1", 6969)
danceID = 0
nodCount = 0
nose1 = 0
y_move = 0
firstFrame = False
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
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

            left_kneeAngle = AngleCalculation.calculate_angle(left_hip, left_knee, left_ankle)
            right_kneeAngle = AngleCalculation.calculate_angle(right_hip, right_knee, right_ankle)
            if not firstFrame:
                firstFrame = True

            nose0 = landmarks[mp_pose.PoseLandmark.NOSE.value].y * height

            tpose_left = AngleCalculation.calculate_angle(left_hip, left_shoulder, left_elbow)
            tpose_right = AngleCalculation.calculate_angle(right_hip, right_shoulder, right_elbow)

            # Setting and displaying properties for angles to be displayed on screen

            # Pose Recognition Logic
            y_move += abs(nose1 - nose0)
            nose1 = nose0

            if (80 < left_kneeAngle < 150) and (80 < right_kneeAngle < 150):
                gesture = "T-POSE"
                print(gesture)
                client.send_message("/DanceMenu", "T-POSE")
                selected = True
                if selected:
                    break
                danceID = math.abs(danceID) % 3
                sys.exit()

            elif 80 < tpose_left < 110:
                gesture = "LEFT"
                print(gesture)
                danceID = (danceID - 1)
                client.send_message("/DanceMenu", "LEFT")

            elif 80 < tpose_right < 110:
                gesture = "RIGHT"
                print(gesture)
                danceID = (danceID + 1)
                client.send_message("/DanceMenu", "RIGHT")
        except:
            pass

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
if selected:
    OSCheck.checkOS("DanceScene", str(danceID))
if not selected:
    Reset.reset()
