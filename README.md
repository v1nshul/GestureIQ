# GestureIQ
- A learning tool which allows you to visualize anything through gestures. 

##  Real-Time Hand Gesture Interaction with TouchDesigner 
This project demonstrates a real-time hand gesture recognition system integrated with TouchDesigner, enabling symbolic manipulation of visuals for enhanced digital interaction—ideal for virtual classrooms, performances, and presentations.

##  Requirements
Software
To run this project smoothly, make sure the following software is installed on your system:

- TouchDesigner (latest stable build)

- Non-Commercial or Commercial license (depending on resolution/output needs)

- Python 3.8+ (TouchDesigner uses an internal Python interpreter, but external scripts or MediaPipe may require this version installed globally)

- MediaPipe (installed via Python)

- OpenCV (for video capture and frame processing)

- Spout (for sending real-time video frames between applications, optional but recommended for integration with OBS or Zoom)

- SpoutCam (optional) – for using TouchDesigner output as a virtual camera source

### Python Packages
  Install the required Python libraries using pip:
  ```pip install mediapipe opencv-python numpy```
  Note: It’s recommended to create a virtual environment for this project.

## Setup Instructions
- Open the .toe file in TouchDesigner.

- Ensure your webcam is connected and recognized.

- Make sure you set up the [mediapipe-touchdesigner](https://github.com/torinmb/mediapipe-touchdesigner.git) plugin.

- Inside TouchDesigner, confirm:

- OSC In DAT or WebSocket DAT is receiving gesture data.

- Render and geometry nodes are active and mapped to gesture inputs.

- (Optional) Install and open SpoutCam to send the output as a virtual webcam.

- In your video conferencing or streaming software (e.g., Zoom, OBS), select SpoutCam or OBS Virtual Camera as the input source.

## Features
- Real-time hand gesture detection using MediaPipe

- Symbolic manipulation of a cube, mapping it's parts into different parts of 3 different shapes.

- Integration with Spout for cross-application video sharing

- Modular network structure for easy customization

## 📂 Folder Structure
```📁 /TouchDesignerGestureProject
 │   ├── main.toe                 # Main TouchDesigner project file
 │   ├── gesture_tracking.py      # Optional external MediaPipe script
 │   └── README.md                # This file
```
### Notes
- Performance may vary based on your CPU/GPU. It is recommended to close unnecessary apps while running real-time rendering.

- If gestures are not recognized, verify camera access and check the OSC/WebSocket connection.

- TouchDesigner Non-Commercial is limited to 1280x1280 resolution.

### Credits
- Developed by Vanshul Kumar
- Hand tracking powered by Google’s MediaPipe and mediapipe-touchdesigner plugin developed by Torin Blakensmith.
- Graphics and interactivity powered by Derivative’s TouchDesigner.
