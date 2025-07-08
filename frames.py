import cv2
import os

video_path = r'C:\mary\OilDetectionProject\ToRunOn.mp4'
frame_rate = 5 # Lower frame_rate means more frames extracted, which can improve training.
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)


frame_id = 0
saved_id = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_id % frame_rate == 0:
        cv2.imwrite(f"{output_dir}/frame_{saved_id:04d}.jpg", frame)
        saved_id += 1
    frame_id += 1

cap.release()
print(f"Extracted {saved_id} frames to {output_dir}/")
