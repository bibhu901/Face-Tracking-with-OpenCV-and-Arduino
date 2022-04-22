import cv2
import serial
import time
#import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
ArduinoSerial=serial.Serial('com7',9600,timeout=0.1)
time.sleep(1)
video_capture = cv2.VideoCapture(0)
fps = video_capture.get(5)
print('Frames per second : ', fps,'FPS')

while video_capture.isOpened():
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        roi_color = frame[y:y+h,x:x+w]
        roi_gray = gray[y:y+h,x:x+w]
        # # smile = smile_cascade.detectMultiScale(roi_gray)
        # # for(sx,sy,sw,sh) in smile:
        # #     cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for(ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    # roi_color = frame[y:y+h,x:x+w]
    # roi_gray = gray[y:y+h,x:x+w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # count=0
    # for(ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    #     count+=1
    #     if(count==2): break
    #plot the squared region in the center of the screen
    cv2.rectangle(frame,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3)

    # Display the resulting frame
    cv2.imshow('video', frame)

    k = cv2.waitKey(1)
    if(k==ord('q')):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()