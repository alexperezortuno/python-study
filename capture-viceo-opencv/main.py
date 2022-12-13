import cv2 as cv


def testDevice(source) -> bool:
    cap = cv.VideoCapture(source)

    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
        return False
    return True


if __name__ == "__main__":
    try:
        for i in range(10):
            if testDevice(i) is True:
                cap = cv.VideoCapture(i)
                while cap.isOpened():
                    ret, frame = cap.read()

                    if ret is True:
                        cv.imshow('frame', frame)
                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break

                cap.release()
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
