# coding=utf-8

import cv2
import numpy as np


def empty():  # callback funtion of trackbar
    pass  # funtion does nothing


def main():
    img = np.zeros([512, 512, 3], np.uint8)  # creating a black canvas or image

    windowname = 'give a wimdow name'

    min_limit = 0  # minimum mlimit of trackbar

    max_limit = 255  # maximum limit of trackbar

    cv2.namedWindow(windowname)  # creating window

    cv2.createTrackbar('Blue', windowname, min_limit, max_limit, empty)  # creating trackbar1 with name Blue

    cv2.createTrackbar('Green', windowname, min_limit, max_limit, empty)  # creating trackbar2 with name Green

    cv2.createTrackbar('Red', windowname, min_limit, max_limit, empty)  # creating trackbar3 with name Red

    while True:
        cv2.imshow(windowname, img)  # displaying image

        b = cv2.getTrackbarPos('Blue', windowname)  # gets current value of 1st trackbar

        g = cv2.getTrackbarPos('Green', windowname)  # gets current value of 1st trackbar

        r = cv2.getTrackbarPos('Red', windowname)  # gets current value of 1st trackbar

        img[:] = [b, g, r]  # assigning the respective BGR color to image pixels

        k = cv2.waitKey(1) & 0xFF  # for 64-bit for 32-bit   "k=waitKey(1)"
        if k == 27:  # comes out of the loop when Esc key is pressed
            break

    cv2.destroyAllWindows()  # closes all windows


main()
