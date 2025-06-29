import time
import cv2
from wrapper_yolo import detect_oil_in_frame

def start_oil_detection_listener(tello):
    print("Oil detection listener started.")

    frame_reader = tello.get_frame_read()

    while True:
        time.sleep(0.1)
        frame = frame_reader.frame

        if frame is None:
            continue

        if detect_oil_in_frame(frame):
            print("Oil detected — drone is hovering!")
            tello.send_rc_control(0, 0, 0, 0)  # Stop movement
            tello.hover()
            time.sleep(10)
            break
