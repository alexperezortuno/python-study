import cv2 as cv
import numpy as np
import pathlib

abs_path = pathlib.Path(__file__).parent.resolve()


def test_rgb1():
    try:
        bgr = np.zeros((300, 300, 3), np.uint8)
        bgr[:] = (255, 0, 0)
        cv.imshow('BGR', bgr)
        cv.waitKey(0)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()


def test_rgb2() -> None:
    try:
        bgr = cv.imread(f'{abs_path}/../images/image002.png')
        gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
        # cv.imshow('BGR', bgr)
        cv.imshow('BGR', gray)
        cv.waitKey(0)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()


if __name__ == "__main__":
    # test_rgb1()
    test_rgb2()
