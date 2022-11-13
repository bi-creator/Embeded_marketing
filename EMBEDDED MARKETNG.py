from fileinput import filename
from gettext import install
from pydoc import synopsis
import sys
import cv2
import os
from datetime import datetime
os.chdir('C:\\Users\\AKASH\\Downloads')
i = 1
#wait = 0
Video = cv2.VideoCapture('catv.mp4')
while True:
    ret, img = Video.read()
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, str(datetime.now()),(20,40),font,2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('live video',img)
    key = cv2.waitKey(25)
    #wait = wait+1
    if key == ord('q'):
        filename = 'Frame_'+str(i)+'.jpg'
        cv2.imwrite(filename,img)
        i = i+1
        #wait = 0
    if key == ord('e'):
        Video.release()
        cv2.destroyAllWindows()