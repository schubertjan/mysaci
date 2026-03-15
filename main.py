import cv2 as cv
from load_imgs import baletka, mysak, zpevacka

cv.namedWindow("Image Window", cv.WINDOW_AUTOSIZE)
while True:
    key = cv.waitKey(1)
    if key != -1:
        key = chr(key).upper()

    if key == "B":
        cv.imshow("Image Window", baletka)
    elif key == "Z":
        cv.imshow("Image Window", zpevacka)
    elif key == "M":
        cv.imshow("Image Window", mysak)
