from func import *
import cv2
import sys
print = sys.stdout.write

density = "@JD%*P+Y$,x. "[::-1]
density ="@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-` "[::-1]

vc = cv2.VideoCapture(0)
w  = vc.get(3)
h = vc.get(4)

ar = w / h
size = int(input("Enter size: "))

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
maxbrt = getBrightness([255 for _ in frame[0,0]])
while rval:
    rval, frame = vc.read() 
    frame = cv2.resize(frame, (size, int(size * ar)))
    for i in range(int(size * ar)):
        for j in range(int(size)):
            brt = getBrightness(frame[i, j])
            avg = int((len(density) - 1) * brt / maxbrt )
            print(fg(*getClosest(frame[i, j])) + density[avg] + ' ')
        print("\n")

    cls()

    #key = cv2.waitKey(10)
    # if key == 27: # exit on ESC
    #     break

cv2.destroyWindow("preview")
vc.release()