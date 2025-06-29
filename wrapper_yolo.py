import cv2
import torch


# Load YOLO model only once
# Note that the path to the weights should be updated to your own local path:
weights_path= 'C:\mary\OilDetectionProject\demo_yolo_oil_detection\oil_detection\weights\best_windows.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path = weights_path, force_reload=False)
model.conf = 0.25  # confidence threshold

def detect_oil_in_frame(frame) -> bool:
    """
    Detects oil spill in a single frame.
    Returns True if oil is detected, else False.
    """
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(rgb)
    detections = results.pandas().xyxy[0]
    return not detections.empty



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