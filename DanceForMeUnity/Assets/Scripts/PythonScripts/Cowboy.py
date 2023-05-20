


def cowpose1(ls, rs, lk):  # left arm and leg raise  3x Left and Right
    # print((60 < ls < 100),(0 < rs < 30),(lk < 120))
    if (60 < ls < 100) and (0 < rs < 30) and (lk < 120):
        return 5
    elif (45 < ls < 120) and (0 < rs < 45) and (lk < 150):
        return 2
    else:
        return 0


def cowpose2(ls, rs, rk):  # right arm and leg raise
    # print((60 < ls < 100),(0 < rs < 30),(rk < 120))
    if (60 < ls < 100) and (0 < rs < 30) and (rk < 120):
        return 5
    elif (45 < ls < 120) and (0 < rs < 45) and (rk < 150):
        return 2
    else:
        return 0


def cowpose3(ls, rs, lk):  # left swing + left leg 4X
    # print((135<ls),(20 < rs < 60),(lk < 150))
    if (135 < ls) and (20 < rs < 60) and (lk < 150):
        return 5
    elif (90 < ls) and (0 < rs < 60) and (lk < 165):
        return 2
    else:
        return 0


def cowpose4(ls, rs, rk):  # right swing + right leg 3X
    # print((135 < rs), (20 < ls < 60), (rk < 150))
    if (135 < rs) and (20 < ls < 60) and (rk < 150):
        return 5
    elif (90 < rs) and (0 < ls < 60) and (rk < 165):
        return 2
    else:
        return 0


def cowpose5(ls, rs, la, ra, lk):  # shovel left down
    # print((160 < la < 180), (160 < ra < 180), (25 < ls < 45), (25 < rs < 45), (lk < 160))
    if (160 < la < 180) and (160 < ra < 180) and (25 < ls < 45) and (25 < rs < 45) and (lk < 160):
        return 5
    elif (150 < la < 180) and (150 < ra < 180) and (15 < ls < 55) and (15 < rs < 55) and (lk < 170):
        return 2
    else:
        return 0


def cowpose6(la, ra):  # shovel up
    #print((la < 40), (ra < 40))
    if (la < 40) and (ra < 40):
        return 5
    elif (la < 60) and (ra < 60):
        return 2
    else:
        return 0

def cowpose7(ls, rs, la, ra, rk):  # shovel right down
    #print((160 < la < 180), (160 < ra < 180), (25 < ls < 45), (25 < rs < 45), (rk < 160))
    if (160 < la < 180) and (160 < ra < 180) and (25 < ls < 45) and (25 < rs < 45) and (rk < 160):
        return 5
    elif (150 < la < 180) and (150 < ra < 180) and (15 < ls < 55) and (15 < rs < 55) and (rk < 170):
        return 2
    else:
        return 0


def cowpose8(ra, rh, n):  # hat tipping
    #print((ra < 90), (rh[1] < n[1]))
    if (ra < 90) and (rh[1] < n[1]):
        return 5
    else:
        return 0


def cowpose9(la, ra, ls, rs, rk):  #arms and leg raise right leg
    #print((150 < la < 180), (150 < ra < 180), (ls < 30), (rs < 30), (rk < 160))
    if (160 < la < 180) and (160 < ra < 180) and (ls < 30) and (rs < 30) and (rk < 160):
        return 5
    elif (140 < la < 180) and (140 < ra < 180) and (ls < 45) and (rs < 45) and (rk < 170):
        return 2
    else:
        return 0


def cowpose10(la, ra, ls, rs, lk):  #arms and leg raise left leg
    #print((150 < la < 180), (150 < ra < 180), (ls < 30), (rs < 30), (lk < 160))
    if (160 < la < 180) and (160 < ra < 180) and (ls < 30) and (rs < 30) and (lk < 160):
        return 5
    elif (140 < la < 180) and (140 < ra < 180) and (ls < 45) and (rs < 45) and (lk < 170):
        return 2
    else:
        return 0


def cowpose11(la, ra, ls, rs, lk):  # leg + shoulder raise (chicken dance) left
    #print((la < 40), (ra < 40), (90 < ls), (90 < rs), (lk < 160))
    if (la < 40) and (ra < 40) and (90 < ls) and (90 < rs) and (lk < 160):
        return 5
    elif (la < 60) and (ra < 60) and (90 < ls) and (90 < rs) and (lk < 170):
        return 2
    else:
        return 0

def cowpose12(la, ra, ls, rs, rk):  # leg + shoulder raise (chicken dance) right
    #print((la < 40), (ra < 40), (90 < ls), (90 < rs), (rk < 160))
    if (la < 40) and (ra < 40) and (90 < ls) and (90 < rs) and (rk < 160):
        return 5
    elif (la < 60) and (ra < 60) and (90 < ls) and (90 < rs) and (rk < 170):
        return 2
    else:
        return 0


def cowpose13(ls, rs):  # left swing
    # print((135<ls),(20 < rs < 60),(lk < 150))
    if (135 < ls) and (20 < rs < 60):
        return 5
    elif (90 < ls) and (0 < rs < 60):
        return 2
    else:
        return 0

def cowpose14(lhZ, rhZ): #left arm pull
    #print((lhZ < rhZ))
    if (lhZ < rhZ):
        return 5
    else:
        return 0

def cowpose15(lhZ, rhZ): #left arm pull
    #print((lhZ > rhZ))
    if (lhZ > rhZ):
        return 5
    else:
        return 0

def cowpose16(ls, rs):
    print((ls > 45), (rs > 45))
    if ((ls > 45) and (rs > 45)):
        return 5
    else:
        return 0

gestureOutputArray3 = ["Pose 1",
                       "Pose 1", "Pose 2", "Pose 1", "Pose 2", "Pose 1", "Pose 2", "Pose 1", "Pose2"
                                                                                             "Pose 1", "Pose 3",
                       "Pose 1", "Pose 3", "Pose 1", "Pose 3", "Pose 1", "Pose 3",
                       "Pose 4", "Pose 4", "Pose 5", "Pose 5",
                       "Pose 6", "Pose 7", "Pose 8", "Pose 7", "Pose 8",
                       "Pose 9", "Pose 10", "Pose 9",
                       "Pose 11", "Pose 12", "Pose 11", "Pose 12",
                       "Pose 13"]

# gestureArray3 = [cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose1(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose2(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose3(left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose4(left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose5(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle, left_kneeAngle),
#                  cowpose6(left_armsAngle, right_armsAngle),
#                  cowpose5(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle, left_kneeAngle),
#                  cowpose6(left_armsAngle, right_armsAngle),
#                  cowpose7(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle, right_kneeAngle),
#                  cowpose6(left_armsAngle, right_armsAngle),
#                  cowpose7(left_shoulderAngle, right_shoulderAngle, left_armsAngle, right_armsAngle, right_kneeAngle),
#                  cowpose6(left_armsAngle, right_armsAngle),
#                  cowpose8(right_armsAngle, right_hand, nose),
#                  cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose9(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose10(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose11(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose11(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, left_kneeAngle),
#                  cowpose12(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose12(left_armsAngle, right_armsAngle, left_shoulderAngle, right_shoulderAngle, right_kneeAngle),
#                  cowpose13(left_shoulderAngle, right_shoulderAngle),
#                  cowpose14(left_handZ, right_handZ),
#                  cowpose15(left_handZ, right_handZ),
#                  cowpose14(left_handZ, right_handZ),
#                  cowpose15(left_handZ, right_handZ),
#                  cowpose6(left_armsAngle, right_armsAngle),  # shovel up similar to pistol hold
#                  ]
