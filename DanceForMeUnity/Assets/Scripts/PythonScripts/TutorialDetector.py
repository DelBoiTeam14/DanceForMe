import cv2
import mediapipe as mp
from pythonosc import udp_client
from datetime import datetime, timedelta
import Reset
import OSCheck
import AngleCalculation

firstFrame = False
leftDetected = False
rightDetected = False
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
posed = False

client = udp_client.SimpleUDPClient("127.0.0.1", 6969)

cap = cv2.VideoCapture(0)
end_time = datetime.now() + timedelta(seconds=60)
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
            right_leg = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            # Calculating angles and storing them to be processed

            tpose_left = AngleCalculation.calculate_angle(left_hip, left_shoulder, left_elbow)
            tpose_right = AngleCalculation.calculate_angle(right_hip, right_shoulder, right_elbow)

            # Pose Recognition Logic
            if (80 < tpose_left < 110) and (80 < tpose_right < 110):
                if leftDetected and rightDetected:
                    client.send_message("/UserDetected", "TPOSE")
                    posed = True
                    break
            elif 80 < tpose_left < 110:
                if rightDetected and not leftDetected:
                    print("Left")
                    client.send_message("/UserDetected", "LEFT")
                    leftDetected = True
            elif 80 < tpose_right < 110:
                if not rightDetected:
                    print("Right")
                    client.send_message("/UserDetected", "RIGHT")
                    rightDetected = True

        except:
            pass

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if posed:
        OSCheck.checkOS("DanceMenu", "TNC")
    if not posed:
        Reset.reset()
