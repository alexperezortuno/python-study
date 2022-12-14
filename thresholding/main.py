import cv2 as cv
import numpy as np
import imutils
import pathlib

abs_path = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    try:
        image = cv.imread(f'{abs_path}/../images/image003.jpg')
        image = imutils.resize(image, width=400)
        _, binary = cv.threshold(image, 170, 255, cv.THRESH_BINARY)
        _, binary_inv = cv.threshold(image, 170, 255, cv.THRESH_BINARY_INV)

        cv.imshow('Image', image)
        cv.imshow('Binary types', np.hstack([binary, binary_inv]))
        cv.waitKey(0)

    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
