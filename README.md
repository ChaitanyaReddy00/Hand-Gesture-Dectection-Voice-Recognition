#  Hand Gesture Detection & Voice Recognition

##  Project Overview

This project is a real-time Hand Gesture Detection and Voice Recognition system developed using Python. It detects hand gestures through a webcam using MediaPipe and OpenCV while simultaneously processing voice commands using PyAudio. The project demonstrates the integration of computer vision and speech processing to build a touchless Human-Computer Interaction (HCI) system.



##  Features

- Real-time hand tracking using MediaPipe
- Detects open palm and finger gestures
- Voice recognition using microphone input
- Live webcam display
- Touchless machine control concept
- Real-time gesture processing
- Easy to extend with additional gestures and voice commands



##  Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAudio
- Speech Recognition



##  Project Structure

```
Hand-Gesture-Detection-Voice-Recognition/
│
├── gesture_voice_control.py
├── README.md
```



##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Hand-Gesture-Detection-Voice-Recognition.git
```

Navigate to the project

```bash
cd Hand-Gesture-Detection-Voice-Recognition
```

Install required libraries

```bash
pip install opencv-python mediapipe numpy pyaudio SpeechRecognition
```



##  Run the Project

```bash
python gesture_voice_control.py
```



##  Gesture Detection

The application captures video through the webcam and detects hand landmarks using MediaPipe.

Example gestures:

- Open Palm → Stop Machine
- Closed Fist → Start Machine
- Additional gestures can be added easily.



##  Voice Recognition

The microphone listens for voice commands and processes them using Speech Recognition.

Example commands:

- Start
- Stop
- Exit



##  Applications

- Smart Home Automation
- Touchless Machine Control
- Robotics
- Human Computer Interaction
- Healthcare Systems
- Industrial Automation



##  Future Enhancements

- More gesture recognition
- AI-based gesture classification
- IoT device integration
- Custom voice assistant
- Mobile application support