from datetime import datetime
from re import S
from turtle import heading, width
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from datetime import datetime

width = GetSystemMetrics(0)

height = GetSystemMetrics(1)


fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

captured_video = cv2.VideoWriter('output.mp4',fourcc,20.0,(width,height))

camera = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    # convert the image into numpy array
    img_np = np.array(img)

    img_res = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    _, frame = camera.read()
    fr_ht,fr_wd, _ = frame.shape
    img_res[0:fr_ht,0:fr_wd,:] = frame[0: fr_ht,0:fr_wd,:]

    cv2.imshow('My capture', img_res)
    #cv2.imshow('camera',frame)
    captured_video.write(img_res)
    if cv2.waitKey(10) == ord('q'):
        break


### This is my screen_recorder by using python