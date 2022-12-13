import cv2 as cv
import pathlib

abs_path = pathlib.Path(__file__).parent.resolve()


if __name__ == "__main__":
    try:
        image = cv.imread(f'{abs_path}/../images/image001.png')
        image2 = cv.imread(f'{abs_path}/../images/image001.png', 0)
        cv.imshow('Image', image)
        cv.imshow('Image2', image2)
        cv.imwrite(f'{abs_path}/../images/image001_copy.png', image2)
        cv.waitKey(0)
    except Exception as e:
        print(e)
    finally:
        cv.destroyAllWindows()
