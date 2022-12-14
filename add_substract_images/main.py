import cv2 as cv
import numpy as np
import pathlib

abs_path = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    try:
        image1 = cv.imread(f'{abs_path}/../images/image004.jpg')
        image2 = cv.imread(f'{abs_path}/../images/image005.jpg')
        # res = cv.add(image1, image2)
        # res = cv.addWeighted(image1, 0.5, image2, 0.5, 0)
        # cv.imshow('Image', res)

        res1 = cv.subtract(image1, image2)
        res2 = cv.absdiff(image1, image2)
        cv.imshow('Image1', np.hstack([res1, res2]))
        cv.imshow('Image2', res1)
        cv.imshow('Image3', res2)
        cv.waitKey(0)
    except KeyboardInterrupt:
        print('Interrupted')
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
