# Explore the dataset by using opencv-python

import numpy as np
import cv2
from pprint import pprint


def paint():
    img = cv2.imread('100_icdar13.png')

    cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def read_file():
    with open('100_icdar13.txt') as fp:
        lines = fp.readlines()
    for line in lines:
        pprint(line)


def main():
    read_file()
