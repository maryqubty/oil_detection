import cv2
import torch

def detect_oil_in_video_frames(
    video_path: str,
    weights_path: str = '/content/drive/MyDrive/yolo5_oilDetection/weights/best.pt',
    conf_threshold: float = 0.25,
    max_frames: int = 5
) -> bool:
    """
    Extracts a few frames from a video and detects oil in them.
    Returns True if oil is detected in any frame.
    """

    # Load model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=False)
    model.conf = conf_threshold

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


# Example usage
video_path = '/content/drive/MyDrive/yolo5_oilDetection/videosToRunOn/Oil_Spill_TrainedOn.MOV'
oil_detected = detect_oil_in_video_frames(video_path)

if oil_detected:
    print("⚠️ Oil detected!")
else:
    print("✅ No oil detected.")
