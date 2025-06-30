import sys
import cv2
from pathlib import Path

# Add YOLOv5 repo to path
yolov5_path = Path(r"C:\mary\OilDetectionProject\yolov5")
sys.path.append(str(yolov5_path))

from models.common import DetectMultiBackend

weights_path = r'C:\mary\OilDetectionProject\demo_yolo_oil_detection\oil_detection\weights\best_windows.pt'
model = DetectMultiBackend(weights_path, device='cpu')
model.conf = 0.25


def detect_oil_in_frame(frame) -> bool:
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = [rgb]  # wrap single image in a list
    results = model(img, augment=False, visualize=False)
    detections = results[0]  # YOLOv5 returns list of Detections per image
    return len(detections.boxes) > 0




'''
# Example usage
video_path = '/content/drive/MyDrive/yolo5_oilDetection/videosToRunOn/Oil_Spill_TrainedOn.MOV'
oil_detected = detect_oil_in_video_frames(video_path)

if oil_detected:
    print("⚠️ Oil detected!")
else:
    print("✅ No oil detected.")
'''