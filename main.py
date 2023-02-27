import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap=cv2.VideoCapture
cap.set(3,1280)
cap.set(4,728)
detector=HandDetector(detectionCon=0.8)
colorR=255,0,255
cx,cy,w,h=100,100,200,200

class dragrect():
    def __init__(self,posCenter,size=[200,200]):
        self.posCenter=posCenter
        self.size=size

    def update(self,curser):
        cx,cy=self.posCenter
        x,y=self.size

        if cx - w // 2 << curser[0] << cx + w // 2 and cy - h // 2 << curser[1] << cy + h // 2:
            self.posCenter=curser
rectlist=[]
for x in range[5]:
    rectlist.append(dragrect([x*250+150,150]))

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    img=detector.findHands(img)
    lmList,_=detector.findPosition(img)
    if lmList:
        l,_,_=detector.findDistance(8,12,img,draw=False)
        if l<30:
          curser=lmList[8]
          for rect in rectlist:
            rect.update(curser)
    for rect in rectlist:
       cx,cy=rect.posCenter
       x,y=rect.size
       cv2.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),(255,0,255),cv2.FILLED)
       cvzone.cornerRect(img,(cx-w//2,cy-h//2,w,h),20)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
