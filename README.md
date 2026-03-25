# 🎓 Face Recognition Attendance System

## 📌 Overview

This project is a Face Recognition-based Attendance System built using Python and OpenCV. It automatically detects and recognizes faces and marks attendance with date and time.

---

## 🚀 Features

* Face Registration (Dataset Creation)
* Model Training using LBPH Algorithm
* Real-time Face Recognition
* Attendance Marking (IN/OUT)
* GUI using Tkinter
* CSV-based attendance storage

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* Pandas
* Tkinter
* PIL

---

## 📂 Project Structure

```
project/

│── dataset/              # Stored face images

│── trainer/              # Trained model

│── attendance.csv        # Attendance records

│── users.csv             # User details

│── register.py           # Face registration

│── train.py              # Model training

│── main.py               # Attendance system
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/face-attendance.git
cd face-attendance
```

2. Install dependencies:

```
pip install opencv-python numpy pandas pillow
```

---

## ▶️ Usage

### Step 1: Register Face

```
python register.py
```

### Step 2: Train Model

```
python train.py
```

### Step 3: Run Attendance System

```
python main.py
```

---

## 📊 Output

* Attendance is saved in `attendance.csv`
* Format: Name | Date | Time | Status

---

## 📌 Example

```
Rohit, 2026-03-26, 10:15:23, IN
```

---

## ⚠️ Requirements

* Webcam
* Good lighting conditions
* Minimum 50 images per user

---

## 🔮 Future Improvements

* Cloud integration
* Mobile app support
* Deep learning models (CNN)
* Face mask detection

---

## 👨‍💻 Author

Rohit Pandey

---

## 📄 License

This project is for educational purposes.
