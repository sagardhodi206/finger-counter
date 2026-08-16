# 🖐️ Finger Counter using Computer Vision

A real-time **Finger Counter** project built using **Python, OpenCV, and MediaPipe**. The system uses a webcam to detect a hand and count the number of raised fingers in real time.

## 🚀 Features

* 🎥 Real-time webcam detection
* 🖐️ Hand detection using MediaPipe
* 🔢 Counts raised fingers from 0 to 5
* ⚡ Real-time processing
* 📺 Displays the finger count on the screen
* 🤖 Computer Vision based system

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## 📁 Project Structure

```text
finger-counter/
│
├── app.py
├── requirements.txt
└── README.md
```

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sagardhodi206/finger-counter.git
```

### 2. Open the Project Folder

```bash
cd finger-counter
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the libraries manually:

```bash
pip install opencv-python mediapipe numpy
```

## ▶️ Run the Project

Run the following command:

```bash
python app.py
```

Your webcam will open and the system will start detecting your hand.

## 🔄 How It Works

```text
Webcam
   ↓
Capture Video Frame
   ↓
MediaPipe Hand Detection
   ↓
Detect Hand Landmarks
   ↓
Identify Raised Fingers
   ↓
Count Fingers
   ↓
Display Count on Screen
```

## 🔢 Finger Counting

The system detects the following number of raised fingers:

| Fingers Raised | Count |
| -------------: | ----: |
|              ✊ |     0 |
|             ☝️ |     1 |
|             ✌️ |     2 |
|             🤟 |     3 |
|             🖖 |     4 |
|            🖐️ |     5 |

## 🎯 Applications

This project demonstrates practical applications of:

* Computer Vision
* Hand Tracking
* Gesture Recognition
* Human-Computer Interaction
* Real-time AI systems

## 🔮 Future Improvements

* Support for both hands
* Count up to 10 fingers
* Gesture-based commands
* Voice feedback
* Integration with other AI projects
* Improved hand tracking

## 👨‍💻 Author

**Sagar Dhodi**

GitHub:
https://github.com/sagardhodi206

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.