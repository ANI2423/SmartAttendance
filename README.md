# 🎓 Smart Attendance System

A **Face Recognition-based Smart Attendance System** built using **Python, OpenCV, and Flask**. This project automates attendance marking by detecting and recognizing faces, storing records in a CSV file, and displaying them through a modern web interface.

---

## 🚀 Features

* 👤 **Face Detection & Recognition**
* 📊 **Automatic Attendance Marking (CSV)**
* 🌐 **Flask Web Dashboard**
* 🕒 **Real-time Date & Time Logging**
* 📁 **Image Dataset Support**
* 🎯 **Live Webcam Detection**

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **Flask**
* **HTML / CSS**
* **CSV**

---

## 📂 Project Structure

```
SmartAttendance/
│
├── backend/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│
├── images/
├── attendance.csv
├── main.py
├── screenshot.png
├── README.md
└── REPORT.md
```

---

## ⚙️ How It Works

1. The webcam captures the user's face.
2. OpenCV processes and detects the face.
3. The system matches it with stored images.
4. If matched:

   * Name is displayed
   * Attendance is saved in CSV
5. Data is shown in the dashboard.

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/your-username/SmartAttendance.git
cd SmartAttendance
```

### 2. Install Dependencies

```
pip install opencv-python flask numpy
```

### 3. Run Face Detection

```
python main.py
```

### 4. Run Web App

```
cd backend
python app.py
```

### 5. Open Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Sample Output

```
Name, Date, Time
Aniruddha, 2026-03-31, 11:15 AM
```

---

## 🔮 Future Improvements

* 🔐 Login System
* ☁️ Database Integration
* 📱 Mobile UI
* 🎯 Deep Learning Face Recognition
* 📊 Analytics Dashboard

---

## 👨‍💻 Author

**Aniruddha Thorat**

---

## 📜 License

This project is for educational purposes.


## ⭐ Conclusion

This project demonstrates how computer vision can automate real-world problems like attendance efficiently using AI-based face recognition.
