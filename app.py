import cv2
import mediapipe as mp

# -------------------------------------------------------------
# 1. INITIALIZE MEDIAPIPE HANDS & OPENCV
# -------------------------------------------------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,                 # Process 1 hand at a time
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Landmark IDs for finger tips and PIP joints
# [Index, Middle, Ring, Pinky]
tip_ids = [8, 12, 16, 20]
pip_ids = [6, 10, 14, 18]

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip horizontally for a natural mirror view
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert BGR frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    finger_count = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Draw hand connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            hand_label = handedness.classification[0].label  # 'Left' or 'Right'

            open_fingers = []

            # -------------------------------------------------------------
            # 2. THUMB LOGIC (Horizontal Movement Check)
            # -------------------------------------------------------------
            # Thumb tip is 4, IP joint is 3
            if hand_label == "Right":
                if landmarks[4].x < landmarks[3].x:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)
            else:  # Left Hand
                if landmarks[4].x > landmarks[3].x:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)

            # -------------------------------------------------------------
            # 3. OTHER 4 FINGERS LOGIC (Vertical Movement Check)
            # -------------------------------------------------------------
            # Compare Y-coordinate of Tip vs PIP joint
            # (Note: Y increases downwards in image coordinates)
            for tip, pip in zip(tip_ids, pip_ids):
                if landmarks[tip].y < landmarks[pip].y:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)

            # Total open fingers count
            finger_count = sum(open_fingers)

            # Draw visual dots on open finger tips
            for idx, tip in enumerate([4] + tip_ids):
                if open_fingers[idx] == 1:
                    cx, cy = int(landmarks[tip].x * w), int(landmarks[tip].y * h)
                    cv2.circle(frame, (cx, cy), 12, (0, 255, 0), cv2.FILLED)

    # -------------------------------------------------------------
    # 4. ON-SCREEN DISPLAY UI
    # -------------------------------------------------------------
    # Draw dark overlay box for text
    cv2.rectangle(frame, (20, 20), (220, 140), (0, 0, 0), cv2.FILLED)
    cv2.rectangle(frame, (20, 20), (220, 140), (0, 255, 0), 2)

    # Display Finger Count Number
    cv2.putText(frame, str(finger_count), (45, 115),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

    # Label Text
    cv2.putText(frame, "FINGERS", (115, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Finger Counter", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()