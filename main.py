import cv2 as cv
from pathlib import Path

root_path = Path(__file__).parent

# Load your image
baletka = cv.imread(str(root_path / "imgs" / "baletka.jpg"))
zpevacka = cv.imread(str(root_path / "imgs" / "zpevacka.jpg"))
mysak = cv.imread(str(root_path / "imgs" / "mysaci.jpg"))
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
