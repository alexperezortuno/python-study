import cv2 as cv
import pathlib

import numpy as np

abs_path = pathlib.Path(__file__).parent.resolve()


def color_detect1() -> None:
    try:
        cap = cv.VideoCapture(0)
        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)

        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                mask1 = cv.inRange(hsv, lowRed1, highRed1)
                mask2 = cv.inRange(hsv, lowRed2, highRed2)
                mask = cv.add(mask1, mask2)

                cv.imshow('mask', mask)
                cv.imshow('frame', frame)

                if cv.waitKey(1)  & 0xFF == ord('q'):
                    break
    except Exception as e:
        print(e)


def color_detect2() -> None:
    try:
        cap = cv.VideoCapture(0)
        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)

        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                mask1 = cv.inRange(hsv, lowRed1, highRed1)
                mask2 = cv.inRange(hsv, lowRed2, highRed2)
                mask = cv.add(mask1, mask2)
                maskRed = cv.bitwise_and(frame, frame, mask=mask)
                cv.imshow('mask', mask)
                cv.imshow('frame', frame)
                cv.imshow('maskRed', maskRed)

                if cv.waitKey(1)  & 0xFF == ord('q'):
                    break
    except Exception as e:
        print(e)


def color_detect3() -> None:
    try:
        cap = cv.VideoCapture(0)
        lowBlue = np.array([100, 150, 20], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                mask = cv.inRange(hsv, lowBlue, highBlue)
                contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                cv.drawContours(frame, contours, -1, (255, 0, 0), 3)

                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
    except Exception as e:
        print(e)


def color_detect4() -> None:
    try:
        cap = cv.VideoCapture(0)
        lowBlue = np.array([80, 150, 20], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                mask = cv.inRange(hsv, lowBlue, highBlue)
                contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                for cnt in contours:
                    area = cv.contourArea(cnt)
                    if area > 3000:
                        new_cnt = cv.convexHull(cnt)
                        cv.drawContours(frame, [new_cnt], 0, (255, 0, 0), 3)

                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
    except Exception as e:
        print(e)


def color_detect5() -> None:
    try:
        cap = cv.VideoCapture(0)
        lowBlue = np.array([80, 150, 20], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                mask = cv.inRange(hsv, lowBlue, highBlue)
                contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                for cnt in contours:
                    area = cv.contourArea(cnt)
                    if area > 3000:
                        M = cv.moments(cnt)
                        if (M['m00'] == 0): M['m00'] = 1
                        x = int(M['m10'] / M['m00'])
                        y = int(M['m01'] / M['m00'])
                        cv.circle(frame, (x, y), 7, (0, 255, 0), -1)
                        font = cv.FONT_HERSHEY_SIMPLEX
                        cv.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.4, (0, 255, 0), 1, cv.LINE_AA)
                        new_cnt = cv.convexHull(cnt)
                        cv.drawContours(frame, [new_cnt], 0, (255, 0, 0), 3)

                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        # color_detect1()
        # color_detect2()
        # color_detect3()
        # color_detect4()
        color_detect5()
    except KeyboardInterrupt:
        print("Shutting down")
