# live_annotated_stream.py

import cv2
import time
from wrapper_yolo import model, pad_to_32
from frame_annotator import annotate_frame_with_boxes

def start_annotated_stream(tello, frame_reader):
    print("Live annotated stream started...")

    try:
        while True:
            frame = frame_reader.frame
            if frame is None or frame.size == 0:
                time.sleep(0.05)
                continue

            try:
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb = pad_to_32(rgb)

                results = model(rgb)
                detections = results.xyxy[0]

                annotated = annotate_frame_with_boxes(frame.copy(), detections, class_names=model.names)

                cv2.imshow("YOLOv5 Live Annotated Stream", annotated)

            except Exception as e:
                print(f"[Stream Error] {e}")
                continue

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.03)

    except Exception as e:
        print(f"[Stream Crash] {e}")

    finally:
        cv2.destroyAllWindows()
        print("Live annotated stream stopped.")
