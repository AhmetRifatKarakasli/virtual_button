import cv2
import mediapipe as mp

webcam=cv2.VideoCapture(0)

el=mp.solutions.hands
el_cizim=mp.solutions.drawing_utils

with el.Hands(static_image_mode=True) as eller:
    while True:
        _,frame=webcam.read()
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=eller.process(rgb)
        yuk,gen,_=frame.shape
        if result.multi_hand_landmarks:
            for cizim in result.multi_hand_landmarks:
                for koordinat in el.HandLandmark:
                    koordinat1=cizim.landmark[8]
                    x = int(koordinat1.x * gen)
                    y = int(koordinat1.y * yuk)
                    cv2.circle(frame,(x,y),5,(0,255,0),-1)

                    if 30<=x<=160 and 30<=y<=120:
                        cv2.rectangle(frame,(30,30),(160,120),(0,0,255),-1)

                    if 430<=x<=560 and 30<=y<=120:
                        cv2.rectangle(frame, (430, 30), (560, 120), (0, 0, 255), -1)

        cv2.putText(frame,"Sol",(30,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
        cv2.rectangle(frame,(30,30),(160,120),(0,0,255),3)

        cv2.putText(frame, "Sag", (430, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        cv2.rectangle(frame, (430, 30), (560, 120), (0, 0, 255), 3)

        cv2.imshow("pencere",frame)
        if cv2.waitKey(5) & 0xFF==ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()



