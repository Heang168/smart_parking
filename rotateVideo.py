import cv2
import numpy as np
cap = cv2.VideoCapture (1)

width = 720
height = 540

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    # flipped = cv2.flip(frame, 1)
    framerot = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # framerot = cv2.resize(framerot, (width, height))
    StackImg = np.hstack([framerot])
    cv2.imshow("ImageStacked", StackImg)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()