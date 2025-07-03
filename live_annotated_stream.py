# live_annotated_stream.py

import cv2
import time
import numpy as np
import torch
from wrapper_yolo import model, pad_to_32

def preprocess_for_stream(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    padded = pad_to_32(rgb)
    img = padded.astype(np.float32) / 255.0
    img = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0)
    return img, padded

def start_annotated_stream(tello, frame_reader):
    print("Live annotated stream started...")

    try:
        cap = frame_reader

        while True:
            frame = cap.frame
            if frame is None or frame.size == 0:
                continue

            try:
                img_tensor, padded_rgb = preprocess_for_stream(frame)

                # Run YOLO detection
                predictions = model(img_tensor)[0]  # get only the first result tensor

                # Draw bounding boxes manually (if any)
                boxes = predictions if isinstance(predictions, torch.Tensor) else []
                padded_bgr = cv2.cvtColor(padded_rgb, cv2.COLOR_RGB2BGR)

                for box in boxes:
                    if len(box) >= 4:
                        x1, y1, x2, y2 = box[:4].tolist()
                        cv2.rectangle(padded_bgr, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)


                # Show frame
                cv2.imshow("YOLOv5 Oil Detection", padded_bgr)

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