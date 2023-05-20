import cv2
import time
start = time.time()
def record():
    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

    while True:
        ret, frame = cap.read()

        writer.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        endTime = time.time()
        ResponseTime = endTime - start

        #Records 2 seconds long of footage
        if ResponseTime > 8:
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

