import time
import cv2
from wrapper_yolo import detect_oil_in_frame

def start_oil_detection_listener(tello, frame_reader, stop_event):
    print("Oil detection listener started.")

    while not stop_event.is_set():  # Optional: stop listener early if event is already set
        time.sleep(0.1)
        frame = frame_reader.frame

        if frame is None or frame.size == 0:
            continue

        if detect_oil_in_frame(frame):
            print("Oil detected — drone is hovering!")
            # tello.send_rc_control(0, 0, 0, 0)
            # tello.hover()
        
