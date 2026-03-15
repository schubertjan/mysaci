import cv2 as cv
from pathlib import Path

root_path = Path(__file__).parent

# Load your image
baletka = cv.imread(str(root_path / "imgs" / "baletka.jpg"))
zpevacka = cv.imread(str(root_path / "imgs" / "zpevacka.jpg"))
mysak = cv.imread(str(root_path / "imgs" / "mysaci.jpg"))
