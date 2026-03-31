import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import winsound
import requests

# 📁 Load Images
path = 'images'
images = []
classNames = []

myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# 🔍 Encode Faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# 🌐 Send to Flask Server
def send_to_server(name):
    try:
        requests.post("http://127.0.0.1:5000/mark", json={"name": name})
    except:
        print("Server not running")

# 📄 Mark Attendance
def markAttendance(name):
    with open('attendance.csv', 'a+') as f:
        f.seek(0)
        data = f.readlines()
        nameList = []

        for line in data:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            dateString = now.strftime('%Y-%m-%d')
            
            f.write(f'\n{name},{dateString},{dtString}')

            # 🔥 Send to dashboard
            send_to_server(name)

            print("Attendance Marked for:", name)
            winsound.Beep(1000, 500)

# ❓ Log Unknown Faces
def logUnknown():
    with open('unknown.csv', 'a+') as f:
        now = datetime.now()
        dt = now.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"UNKNOWN,{dt}\n")

# 🔥 Encode all known faces
encodeListKnown = findEncodings(images)
print("Encoding Complete")

# 🎥 Start Camera
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.5:
            name = classNames[matchIndex].upper()

            # ✅ Mark attendance
            markAttendance(name)

            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,name,(x1,y2+30),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        else:
            name = "UNKNOWN"

            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.putText(img,name,(x1,y2+30),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

            # 🔥 Log unknown separately
            logUnknown()

    cv2.imshow('Webcam', img)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()