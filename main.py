import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import winsound

path = 'images'
images = []
classNames = []

myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


# 🔥 ADD THIS BELOW
def captureNewStudent(img):
    global images, classNames, encodeListKnown

    name = input("Enter student name: ").lower()

    file_path = f'images/{name}.jpg'
    cv2.imwrite(file_path, img)

    print(f"{name} added successfully!")

    # Reload images
    images = []
    classNames = []
    myList = os.listdir('images')

    for cl in myList:
        curImg = cv2.imread(f'images/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

    encodeListKnown = findEncodings(images)
    print("Encodings updated!")


import winsound   # at top

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

            print("Attendance Marked for:", name)  # DEBUG

            # 🔊 SOUND HERE
            winsound.Beep(1000, 500)

encodeListKnown = findEncodings(images)
print("Encoding Complete")

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
            markAttendance(name)
        else:
            name = "UNKNOWN"

            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,name,(x1,y2+30),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            cv2.putText(img, 'Attendance Marked',
            (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
            (0,255,0), 2)

            markAttendance(name)

    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break