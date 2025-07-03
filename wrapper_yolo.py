import sys
import cv2
from pathlib import Path
import torch
import numpy as np
import time
from frame_annotator import annotate_frame_with_boxes

# Add YOLOv5 repo to path
yolov5_path = Path(r"C:\mary\OilDetectionProject\yolov5")
sys.path.append(str(yolov5_path))

# Load YOLOv5 model using torch.hub (custom-trained)
weights_path = r"C:\mary\OilDetectionProject\demo_yolo_oil_detection\oil_detection\weights\best_windows.pt"
model = torch.hub.load(str(yolov5_path), 'custom', path=weights_path, source='local')
model.conf = 0.25  # Confidence threshold

# Create folder for saving annotated frames
SAVE_DIR = Path("annotated_frames")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# Resize to nearest multiple of 32
def pad_to_32(img):
    h, w = img.shape[:2]
    new_h = (h + 31) // 32 * 32
    new_w = (w + 31) // 32 * 32
    return cv2.resize(img, (new_w, new_h))

# Oil detection function with frame saving
def detect_oil_in_frame(frame) -> bool:
    if frame is None or frame.size == 0:
        print("[Warning] Empty or invalid frame received.")
        return False

    try:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = pad_to_32(rgb)
    except cv2.error as e:
        print(f"[OpenCV Error] Failed to process frame: {e}")
        return False

    # Inference using Ultralytics model (auto handles tensor conversion)
    try:
        results = model(rgb)
        detections = results.xyxy[0]  # tensor of detections: (n,6) [x1,y1,x2,y2,conf,class]

        if detections.shape[0] > 0:
            annotated = annotate_frame_with_boxes(frame.copy(), detections, class_names=model.names)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = SAVE_DIR / f"oil_detected_{timestamp}.jpg"
            cv2.imwrite(str(filename), annotated)
            print(f"[Saved] Annotated frame saved to: {filename}")
            return True
        else:
            return False

    except Exception as e:
        print(f"[Detection Error] {e}")
        return False
