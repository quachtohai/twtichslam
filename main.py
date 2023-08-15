import cv2
from display import Display
from extractor import Extractor

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
H = 1080//2
W = 1920//2
disp = Display(W, H)

fe = Extractor()
def process_frame(img):
    img = cv2.resize(img, (W, H))
    matches = fe.extract(img)
    for pt1, pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1)
        u2, v2 = map(lambda x: int(round(x)), pt2)
        # cv2.circle(img, (u1, v1),  color=(255, 255, 0), radius=3)
        cv2.line(img, (u1, v1), (u2, v2),  color=(255, 255, 0))

    disp.paint(img)


if __name__ =="__main__":
    cap = cv2.VideoCapture("test.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break