import cv2
import mediapipe as mp
import pyaudio
import json
import vosk

# Initialize MediaPipe for Hand Tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Load Vosk Model for Speech Recognition
model = vosk.Model("vosk-model-en-us-0.22")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize Microphone for Voice Input
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Open Camera for Hand Gesture Detection
cap = cv2.VideoCapture(0)

print("Listening for voice commands and detecting hand gestures...")

while True:
    # Voice Recognition
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        command = result["text"]
        print("You said:", command)

        # Perform Actions Based on Voice Command
        if "start" in command:
            print("✅ Machine Started")
        elif "stop" in command:
            print("🛑 Machine Stopped")

    # Hand Gesture Recognition
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB and Process with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract Landmarks for Gesture Recognition
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

            # Detect Thumbs-Up Gesture
            if thumb_tip < index_tip:  # Thumb is above index finger
                print("👍 Detected Thumbs Up - Starting Machine")
            
            # Detect Open Palm Gesture
            elif all(hand_landmarks.landmark[i].y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y for i in range(1, 5)):
                print("✋ Detected Open Palm - Stopping Machine")

    # Display the Camera Feed
    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
mic.terminate()