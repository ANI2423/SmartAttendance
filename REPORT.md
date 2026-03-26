# 📄 Smart Attendance System using Face Recognition

---

## 📝 1. Introduction

Attendance management is an essential task in educational institutions and organizations. Traditional methods such as manual roll calls are time-consuming and prone to errors. This project introduces an automated attendance system using face recognition technology to improve efficiency and accuracy.

---

## 🎯 2. Problem Statement

Manual attendance systems:

* Consume time
* Are prone to proxy attendance
* Require human effort

There is a need for an automated, reliable, and contactless system.

---

## 💡 3. Proposed Solution

The proposed system uses computer vision and face recognition to identify individuals and automatically mark attendance. The system captures live video, detects faces, and compares them with stored images.

---

## ⚙️ 4. Methodology

The working of the system involves the following steps:

1. Load images of known individuals
2. Encode facial features using face_recognition
3. Start webcam for real-time video capture
4. Detect faces in each frame
5. Compare detected faces with known encodings
6. If matched → mark attendance
7. If not matched → show "UNKNOWN"
8. Allow adding new student dynamically

---

## 🛠️ 5. Technologies Used

* Python
* OpenCV
* face_recognition (dlib)
* NumPy
* CSV file handling

---

## 📊 6. Results

The system successfully:

* Detects faces in real-time
* Recognizes known individuals
* Marks attendance with timestamp
* Stores data efficiently in CSV

---

## ⚠️ 7. Challenges Faced

* Installing dlib and face_recognition
* Handling lighting variations
* Ensuring real-time performance
* Managing unknown faces

---

## 🔮 8. Future Scope

* GUI-based interface
* Database integration (MySQL/Firebase)
* Mask detection feature
* Mobile application integration
* Multi-camera support

---

## 🏁 9. Conclusion

The Smart Attendance System demonstrates how computer vision can automate real-world problems efficiently. It reduces manual effort, increases accuracy, and provides a scalable solution for attendance management.

---

## 👨‍💻 10. Author

Aniruddha Thorat
Computer Vision BYOP Project
