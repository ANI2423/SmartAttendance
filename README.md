# 🎓 Smart Attendance System using Face Recognition

## 📌 Overview

The Smart Attendance System is an AI-based application that automates attendance marking using real-time face recognition. It eliminates manual attendance processes and improves efficiency, accuracy, and reliability.

---

## 🚀 Features

* ✅ Real-time face detection and recognition
* ✅ Automatic attendance marking with date & time
* ✅ CSV-based attendance storage
* ✅ 🔊 Beep sound confirmation
* ✅ ❌ Unknown face detection
* ✅ ➕ Add new student dynamically (Press **N**)
* ✅ User-friendly interface with bounding boxes

---

## 🛠️ Tech Stack

* Python
* OpenCV
* face_recognition (dlib-based)
* NumPy
* OS & Datetime

---

## 📂 Project Structure

```
SmartAttendance/
│
├── images/              # Student images
├── attendance.csv       # Attendance records
├── main.py              # Main code
├── working_demo.png     # Screenshot
├── README.md
```

---

## ⚙️ Installation

1. Clone repository:

```
git clone https://github.com/ANI2423/SmartAttendance.git
cd SmartAttendance
```

2. Install dependencies:

```
pip install opencv-python face-recognition numpy
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 🎮 Controls

| Key | Function        |
| --- | --------------- |
| N   | Add new student |
| Q   | Quit system     |

---

## 🧠 Working Principle

* Webcam captures real-time video
* Face detection & encoding
* Matches with stored images
* Marks attendance in CSV
* Plays beep sound on success
* Allows dynamic student addition

---

## 📸 Working Demo

![Working Screenshot](working_demo.png)

---

## 📊 Sample Output

```
ANIRUDDHA,2026-03-26,10:32:15
RAHUL,2026-03-26,10:35:02
```

---

## ⚠️ Limitations

* Depends on lighting conditions
* Requires clear face images
* Accuracy may reduce with angle variations

---

## 🔮 Future Scope

* GUI-based system
* Cloud/database integration
* Mask detection
* Mobile app support

---

## 👨‍💻 Author

Aniruddha Thorat
Computer Vision BYOP Project

---

## ⭐ Conclusion

This project demonstrates how computer vision can automate real-world problems like attendance efficiently using AI-based face recognition.
