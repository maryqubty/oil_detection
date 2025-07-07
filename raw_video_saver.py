import cv2
import time
from pathlib import Path

'''
This module saves raw video frames from a Tello drone's camera feed for training pourposes.
It captures frames for a specified duration and saves them to an AVI file.
'''
def save_raw_video(tello, frame_reader, duration=30, output_path="saved_videos/raw_capture.avi"):
    print("[Raw Video Saver] Starting video recording...")

    # Wait for a valid frame
    while True:
        frame = frame_reader.frame
        if frame is not None and frame.size > 0:
            break
        time.sleep(0.1)

    height, width = frame.shape[:2]
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Or 'MJPG'/'MP4V'
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (width, height))

    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            frame = frame_reader.frame
            if frame is not None and frame.size > 0:
                out.write(frame)
            time.sleep(0.03)

    except Exception as e:
        print(f"[Raw Video Saver Error] {e}")

    finally:
        out.release()
        print(f"[Raw Video Saver] Saved to {output_path}")
