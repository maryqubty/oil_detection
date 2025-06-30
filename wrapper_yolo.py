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




# Function to detect oil in video frames using YOLOv5
def detect_oil_in_video_frames(
    video_path: str,
    max_frames: int = 5
) -> bool:
    """
    Extracts a few frames from a video and detects oil in them.
    Returns True if oil is detected in any frame.
    """
    # Open video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Failed to open video: {video_path}")
        return False

    frame_count = 0
    while frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run detection
        results = model(rgb_frame)
        detections = results.pandas().xyxy[0]

        if not detections.empty:
            cap.release()
            return True  # Oil detected

        frame_count += 1

    cap.release()
    return False  # No oil in sampled frames

'''
# Example usage
video_path = '/content/drive/MyDrive/yolo5_oilDetection/videosToRunOn/Oil_Spill_TrainedOn.MOV'
oil_detected = detect_oil_in_video_frames(video_path)

if oil_detected:
    print("⚠️ Oil detected!")
else:
    print("✅ No oil detected.")
'''