# live_annotated_stream.py

import cv2
import time
import numpy as np
from wrapper_yolo import model

def start_annotated_stream(tello):
    print("Live annotated stream started...")

    try:
        cap = tello.get_frame_read()

        while True:
            frame = cap.frame
            if frame is None:
                continue

            # Run YOLOv5 detection
            results = model(frame)
            annotated = results.render()[0]

            # Display annotated frame
            cv2.imshow("YOLOv5 Oil Detection", annotated)

            # Exit on 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.03)  # ~30 FPS

    except Exception as e:
        print(f"Error during live stream: {e}")

    finally:
        cv2.destroyAllWindows()
        print("Live annotated stream stopped.")
