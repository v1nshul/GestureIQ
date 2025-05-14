'''
Author : Vanshul Kumar
Purpose : This is the draft code that combines mediapipe and OpenCV library to 
          create gesture tracking and symbols on the screen
'''

import mediapipe as mp                                                        # importing mediapipe and OpenCV          
import cv2

mp_hands = mp.solutions.hands                                                 # initializing MediaPipe hand tracking
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)


gesture_actions = {                                                           # defining gesture-action mapping
    "thumbs_up": "create a circle",
    "thumbs_down" : "remove circle"
}


def is_thumbs_up(hand_landmarks):                                             # function to detect thumbs up
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
    return thumb_tip.y < thumb_mcp.y


def is_thumbs_down(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
    return thumb_tip.y > thumb_mcp.y


cap = cv2.VideoCapture(0)                                                       # processing input video 
circle_active = False
circle_position = (0,0) 

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break
    
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))             # processing the image with MediaPipe

    gesture_text = ""
    
    if results.multi_hand_landmarks:                                            # extracting hand landmarks and recognize gestures
        for hand_landmarks in results.multi_hand_landmarks:
            if is_thumbs_up(hand_landmarks):
                print("Detected gesture: thumbs_up")
                gesture_text = "Thumbs up"
                if "thumbs_up" in gesture_actions:
                    circle_active = True
                    action = gesture_actions["thumbs_up"]
                    print(f"Performing action: {action}")
                                                                                # Updating circle position based on the tip position
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                height, width, _ = image.shape                                  # Converting normalized coordinates to pixel values
                circle_position = (int(index_finger_tip.x * width), int(index_finger_tip.y * height))

            elif is_thumbs_down(hand_landmarks):
                gesture_text = "Thumbs Down"                                    # text to display
                circle_active = False                                           # disabling the circle on thumbs down
                if "thumbs_down" in gesture_actions:
                    action = gesture_actions["thumbs_down"]
                    print(f"Performing action: {action}")
            else:
                print('None')
                gesture_text = "None"
                circle_active = False
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if gesture_text:
        cv2.putText(image, f"Detected gesture: {gesture_text}", (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    if circle_active:                                                           # drawing the circle at the updated position
        radius = 50
        color = (0, 255, 0)  
        thickness = 2 
        cv2.circle(image, circle_position, radius, color, thickness)

    cv2.imshow('MediaPipe Hands', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
