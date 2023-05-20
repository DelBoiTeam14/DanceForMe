import cv2
import numpy as np
import mediapipe as mp


def pose1(ra, rs, la, ls):
    if (40 < rs < 90) and (100 < ra < 150) and (40 < ls < 90) and (100 < la < 150):
        return 5
    elif (30 < rs < 100) and (90 < ra < 160) and (30 < ls < 100) and (90 < la < 160):
        return 2
    else:
        return 0


def pose2(ra, rs, la, ls):
    # print((70 < rs < 110) , (160 < ra) , (70 < ls < 110) , (160 < la))
    if (60 < rs < 110) and (150 < ra) and (60 < ls < 110) and (150 < la):
        return 5
    elif (70 < rs < 110) and (90 < ra < 110) and (70 < ls < 110) and (90 < la < 110):
        return 2
    else:
        return 0


def pose3(ra, rk):
    if (ra < 90) and (rk < 160):
        return 5
    elif (ra < 110) and (rk < 170):
        return 2
    else:
        return 0

def pose4(la, lk):
    if (la < 90) and (lk < 160):
        return 5
    elif (la < 110) and (lk < 170):
        return 2
    else:
        return 0


# could bring in z into the following functions
def pose5(lk, rk, ra, la):

    if ((lk < 120) or rk < 120) and (ra < 160) and (la < 160):
        return 5
    elif (lk < 120) and (ra < 160) and (la < 160):
        return 2
    else:
        return 0


# is this the correct knee
def pose6(lk, rk, ra, la):
    if ((lk < 120) or rk < 120) and (ra < 160) and (la < 160):
        return 5
    elif ((lk < 120) or rk < 120) and (ra < 160) and (la < 160):
        return 2
    else:
        return 0


def pose7(rs, ls, ra, la):

    if (140 < la) and (70 < ls) and (rs < 40) and (ra < 110):
        return 5
    elif (130 < la) and (60 < ls) and (rs < 50) and (ra < 120):
        return 2
    else:
        return 0


def pose8(rs, ls, ra, la):
    if (140 < ra) and (70 < rs) and (ls < 40) and (la < 110):
        return 5
    elif (130 < ra) and (60 < rs) and (ls < 50) and (la < 120):
        return 2
    else:
        return 0


def pose10(la, ls, rs, ra):
    if (100 < ls) and (150 < la) and (rs < 90) and (60 < ra < 120):
        return 5
    elif (100 < ls) and (150 < la) and (rs < 90) and (60 < ra < 120):
        return 2
    else:
        return 0


def pose11(la, ls, rs, ra):
    if (ls < 50) and (140 < la) and (rs < 100) and (80 < ra < 130):
        return 5
    elif (ls < 50) and (150 < la) and (rs < 90) and (60 < ra < 120):
        return 2
    else:
        return 0


# pose 12 is repeat of pose 10
# pose 13 is a repeat of pose 11

# need to check the animations of the combination of the 2 files


################################################


def pose21(ra, rs, la, ls):
    if (160 < ra) and (110 < rs) and (ls < 90) and (la < 70):
        return 5
    elif (ra < 170) and (120 < rs) and (ls < 100) and (la < 80):
        return 2
    else:
        return 0


def pose22(ra, rs, la, ls):
    #print((110 < rs) , (ra < 70) , (160 < la) , (ls < 90))
    if (90 < rs) and (ra < 70) and (160 < la) and (ls < 90):
        return 5
    elif (80 < rs) and (ra < 80) and (150 < la) and (ls < 100):
        return 2
    else:
        return 0


def pose23(ra, rs, la, ls):
    if (90 > rs) and (160 < ra) and (la < 70) and (90 < ls):
        return 5
    elif (100 > rs) and (150 < ra) and (la < 80) and (80 < ls):
        return 2
    else:
        return 0


def pose24(ra, rs, la, ls):
    if (90 > rs) and (160 < ra) and (la < 70) and (90 < ls):
        return 5
    elif (100 > rs) and (150 < ra) and (la < 80) and (80 < ls):
        return 2
    else:

        return 0


def pose25(rk, ra, la, ls):
    if (rk < 160) and (25 < ra < 75) and (90 < la < 140) and (20 < ls):

        return 5
    elif (rk < 170) and (15 < ra < 85) and (70 < la < 160) and (10 < ls):
        return 2
    else:

        return 0


def pose26(lk, la, ra, rs):
    if (lk < 160) and (25 < la < 75) and (90 < ra < 140) and (20 < rs):
        return 5
    elif (lk < 170) and (15 < la < 85) and (70 < ra < 160) and (10 < rs):
        return 2
    else:

        return 0


# could add a second hand movement function
def pose27(rk, ra, la, lHip):
    #print((rk < 160) , (30 < ra < 70) , (160 < lHip))
    if (rk < 160) and (30 < ra < 70) and (160 < lHip):

        return 5
    elif (rk < 170) and (20 < ra < 80) and (160 < lHip):

        return 2
    else:

        return 0


def pose28(rk, ra, la, lHip, ls):
    print((rk < 160) , (160 < lHip) , (70 < la < 110) , (25 < ls))
    if (rk < 160) and (160 < lHip) and (70 < la < 110) and (25 < ls):

        return 5
    elif (rk < 170) and (160 < lHip) and (60 < la < 120) and (15 < ls):

        return 2
    else:

        return 0


# stand straight Box Pose
# no rotaional shoulder pos yet
def pose29(rhx, rhy, rHipx, rHipy, lHipx, lHipy, lex, ley):
    if (lex > rhx) and (lex + 2 * (rHipx - lHipx)) < rhx and (ley - (rHipx - lHipx)) > rhy and (
            ley + 0.5 * (rHipx - lHipx) < rhy):
        return 5
    elif (lex > rhx) and (lex + 4 * (rHipx - lHipx)) < rhx and (ley - (rHipx - lHipx)) > rhy and (
            ley + 2 * (rHipx - lHipx) < rhy):
        return 2
    else:
        return 0


# stand straight Box Pose
# no rotaional shoulder pos yet
def pose210(lhx, lhy, rHipx, rHipy, lHipx, lHipy, rex, rey):
    if (rex > lhx) and (rex + 2 * (rHipx - lHipx)) < lhx and (rey - (rHipx - lHipx)) > lhy and (
            rey + 0.5 * (rHipx - lHipx) < lhy):
        return 5
    elif (rex > lhx) and (rex + 4 * (rHipx - lHipx)) < lhx and (rey - (rHipx - lHipx)) > lhy and (
            rey + 2 * (rHipx - lHipx) < lhy):
        return 2
    else:
        return 0


def pose211(lHandPosy, rHandPosy, Nosey):
    # print((lHandPosy < Nosey) , (Nosey < rHandPosy))
    if (lHandPosy < Nosey) and (Nosey < rHandPosy):

        return 5

    elif (rHandPosy < Nosey) and (Nosey < lHandPosy):
        return 2
    else:

        return 0
