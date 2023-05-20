import cv2
import numpy as np
import mediapipe as mp
# from DanceSeriesClean import *


def balletpose1(ls, rs, la, ra):  # ballet hand on stomach
    # print((25 < ls < 65), (25 < rs < 65), (70 < la < 130), (70 < ra < 130))
    if (25 < ls < 65) and (25 < rs < 65) and (80 < la < 130) and (80 < ra < 130):
        return 5
    elif (15 < ls < 75) and (15 < rs < 75) and (70 < la < 140) and (70 < ra < 140):
        return 2
    else:
        return 0


def balletpose2(lk, rk):  # bend down
    # print((lk < 150), (rk < 150))
    if (lk < 150) and (rk < 150):
        return 5
    elif (lk < 165) and (rk < 165):
        return 2
    else:
        return 0


def balletpose3(rs, rh):  # right arm and right leg raise
    # print((135 < rs < 180), (rh < 150))
    if (135 < rs < 180) and (rh < 150):
        return 5
    elif (90 < rs < 180) and (rh < 165):
        return 2
    else:
        return 0


def balletpose4(ls, lh):  # left arm and left leg raise
    # print((135 < ls < 180), (lh < 150))
    if (135 < ls < 180) and (lh < 150):
        return 5
    elif (90 < ls < 180) and (lh < 165):
        return 2
    else:
        return 0


def balletpose5(lh, rh, ls, rs):  # tip toe jump -> comeback later
    if (70 < lh < 120) and (150 < rh < 200):
        if (70 < ls < 120) and (150 < rs < 220):
            gesture = "Ballet Pose 5"
            return gesture
    else:
        gesture = "No pose"
        return gesture


def balletpose6(la, ra, ls, rs):  # arms up
    # print((100 < ls), (100 < rs), (45 < la < 135), (45 < ra < 135))
    if (100 < ls) and (100 < rs) and (45 < la < 135) and (45 < ra < 135):
        return 5
    elif (80 < ls) and (80 < rs) and (35 < la < 145) and (35 < la < 145):
        return 2
    else:
        return 0


def balletpose7(ls, rs, la, ra, lk):  # ballet down left
    # print((160 < la < 180), (160 < ra < 180), (25 < ls < 45), (25 < rs < 45), (lk < 160))
    if (160 < la < 180) and (160 < ra < 180) and (25 < ls < 45) and (25 < rs < 45) and (lk < 160):
        return 5
    elif (150 < la < 180) and (150 < ra < 180) and (15 < ls < 55) and (15 < rs < 55) and (lk < 170):
        return 2
    else:
        return 0


def balletpose8(ls, rs, lh):  # arm and left leg raise
    # print((135 < ls < 180), (100 < rs < 180), (lh < 150))
    if (135 < ls < 180) and (100 < rs < 180) and (lh < 150):
        return 5
    elif (90 < ls < 180) and (70 < rs < 180) and (lh < 165):
        return 2
    else:
        return 0


def balletpose9(ls, rs, rh):  # arm and right leg raise
    # print((135 < rs < 180), (100 < ls < 180), (rh < 150))
    if (135 < rs < 180) and (100 < ls < 180) and (rh < 150):
        return 5
    elif (90 < rs < 180) and (70 < ls < 180) and (rh < 165):
        return 2
    else:
        return 0


def balletpose10(ls, rs):  # arms up only
    # print((50 < ls < 90), (100 < rs))
    if (50 < ls < 90) and (100 < rs):
        return 5
    elif (40 < ls < 100) and (90 < rs):
        return 2
    else:
        return 0


def balletpose11(ls, rs):  # arms pointing down but not by side
    print((40 < ls < 80), (40 < rs < 80))
    if (40 < ls < 80) and (40 < rs < 80):
        return 5
    elif (30 < ls < 90) and (30 < rs < 90):
        return 2
    else:
        return 0


gestureOutputArray1 = ["Ballet Pose 1", "Ballet Pose 2", "Ballet Pose 3", "Ballet Pose 4", "Ballet Pose 1",
                       "Ballet Pose 2", "Ballet Pose 5", "Ballet Pose 1",
                       "Ballet Pose2", "Ballet Pose 1", "Ballet Pose 2", "Ballet Pose 1", "Ballet Pose 2",
                       "Ballet Pose 1", "Ballet Pose 2",
                       "Ballet Pose 1", "Ballet Pose 2", "Ballet Pose 1"]

# gestureArray1 = [balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose3(left_hipsAngle, right_hipsAngle), balletpose4(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose5(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle),
#                               balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose1(left_armsAngle, right_armsAngle), balletpose2(left_hipsAngle, right_hipsAngle, left_shoulderAngle, right_shoulderAngle),
#                               balletpose6(left_armsAngle, right_armsAngle)]
