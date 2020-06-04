import cv2
import numpy as np
cap = cv2.VideoCapture('sentry3.mkv')
while cap.isOpened():
    ret1,frame = cap.read()
    if ret1 == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_b = np.array([0,0,156])
        u_b = np.array([255,20,178])
        msk = cv2.inRange(hsv, l_b, u_b)
        mask = cv2.GaussianBlur(msk,(5,5),0)
        res = cv2.bitwise_and(frame,frame,mask=mask)
        ret,thresh = cv2.threshold(mask,127,255,0)
        contours,hierarchy = cv2.findContours(thresh, 1, 2)
        #x1,y1,w1,h1 = cv2.boundingRect(cnt1)
        #x2,y2,w2,h2 = cv2.boundingRect(cnt2)
        #cv2.rectangle(frame, (x1,y1), (x1+w1,y1+h1),(0,255,0),2)
        #cv2.drawContours(frame,contours,-1,(0,255,0),2)
        cnt = sorted(contours, key=lambda x: cv2.contourArea(x),reverse=True)
        try:
            for c in (cnt[0],cnt[1]):
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        except:
            pass
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
    else :
        pass
    if cv2.waitKey(42) == 27: #fps=24;(1/fps)*1000=41.67
        cv2.destroyAllWindows()
        break
