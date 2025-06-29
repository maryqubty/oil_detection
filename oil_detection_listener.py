# oil_detection_listener.py

import time
import cv2
import numpy as np
from wrapper_yolo import detect_oil_in_frame

def start_oil_detection_listener(video, tello):
    print("🟢 Oil detection listener started.")
    
    while True:
        time.sleep(0.1)

        # Get latest JPEG frame
        jpeg_bytes = video.jpeg_frame
        if not jpeg_bytes:
            continue

        # Decode the frame
        frame_array = np.frombuffer(jpeg_bytes, dtype=np.uint8)
        frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

        # Detect oil
        if detect_oil_in_frame(frame):
            print("⚠️ Oil detected — landing triggered by external listener!")
            tello.command('stop')
            print("🛑 Drone stopped and is hovering over oil.")
            time.sleep(10)
            break
