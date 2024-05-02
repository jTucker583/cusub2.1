import cv2
 

cam = cv2.VideoCapture(0)
num = 1

try:
    while(num < 11):
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        cv2.imwrite("taskScripts/Photogrammetry/photos/photo%d.jpg" % num, frame)
        num += 1
        cv2.waitKey(1000)
except KeyboardInterrupt:
    pass

cam.release()
cv2.destroyAllWindows()