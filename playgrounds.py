import cv2

from readfile import read_points

if __name__ == '__main__':
    # get current frame from webcam
    img = cv2.imread('data/demo/p23-181.png')
    my_list = read_points('data/res/p23-181.txt')

    for i in my_list:
        for j in i:
            cv2.circle(img, j, 10, (0, 0, 255), -1)

    cv2.imshow('demo', img)

    cv2.waitKey(0)
    cv2.destroyWindow('YRB_calib')
