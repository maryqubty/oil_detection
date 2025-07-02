# wrapper_yolo.py
import sys
import cv2
from pathlib import Path
import torch
import numpy as np

# Add YOLOv5 repo to path
yolov5_path = Path(r"C:\mary\OilDetectionProject\yolov5")
sys.path.append(str(yolov5_path))

from models.common import DetectMultiBackend

weights_path = r'C:\mary\OilDetectionProject\demo_yolo_oil_detection\oil_detection\weights\best_windows.pt'
model = DetectMultiBackend(weights_path, device='cpu')
model.conf = 0.25

# Round dimensions to nearest multiple of 32
def pad_to_32(img):
    h, w = img.shape[:2]
    new_h = (h + 31) // 32 * 32
    new_w = (w + 31) // 32 * 32
    return cv2.resize(img, (new_w, new_h))

# Function to detect oil in a single frame
def detect_oil_in_frame(frame) -> bool:
    if frame is None or frame.size == 0:
        print("[Warning] Empty or invalid frame received.")
        return False

    try:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except cv2.error as e:
        print(f"[OpenCV Error] Failed to convert frame to RGB: {e}")
        return False
    
    # Resize to a valid shape that avoids tensor mismatch
    rgb = pad_to_32(rgb)  # ← ADD THIS LINE HERE

    # Normalize and convert to tensor, since yolo5 expects shape (B, C, H, W) and not (H, W, C).
    img = rgb.astype(np.float32) / 255.0
    img = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0)  # (1, 3, 640, 640)

    # Run through model
    results = model(img, augment=False, visualize=False)

    try:
        detections = results[0]  # This is a tensor
        return detections.shape[0] > 0  # if any detections exist

    except Exception as e:
        print(f"[Detection Error] {e}")
        return False
