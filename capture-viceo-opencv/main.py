import cv2 as cv
import pathlib

abs_path = pathlib.Path(__file__).parent.resolve()


def testDevice(source) -> bool:
    cap = cv.VideoCapture(source)

    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
        return False
    return True


def capture() -> None:
    try:
        for i in range(10):
            if testDevice(i) is True:
                cap = cv.VideoCapture(i)
                out = cv.VideoWriter(f'{abs_path}/../captures/output.avi', cv.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
                while cap.isOpened():
                    ret, frame = cap.read()

                    if ret is True:
                        cv.imshow('frame', frame)
                        out.write(frame)
                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break

                cap.release()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        cv.destroyAllWindows()


def read() -> None:
    try:
        for i in range(10):
            if testDevice(i) is True:
                cap = cv.VideoCapture(f'{abs_path}/../captures/output.avi')
                while cap.isOpened():
                    ret, frame = cap.read()

                    if ret is True:
                        cv.imshow('frame', frame)
                        if cv.waitKey(30) & 0xFF == ord('q'):
                            break
                    else:
                        break

                cap.release()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        cv.destroyAllWindows()


if __name__ == "__main__":
    capture()
