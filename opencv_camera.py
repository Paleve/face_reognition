import cv2
import os
import numpy as np


cap = cv2.VideoCapture(0)
c = 1
timeF = 2
name = 'tsy'
path = './data/' + name

if not os.path.isdir(path):
    os.mkdir(path)

while True:
    ret,frame = cap.read()
    if (c % timeF == 0):
        cv2.imwrite(path+'/'+name + '_' + str(c) + '.jpg', frame)

    cv2.imshow('frame',frame)
    c += 1
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()