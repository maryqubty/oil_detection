import cv2
from pathlib import Path

def split_video(input_path, output_path, start_time_sec, end_time_sec):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Failed to open video: {input_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time_sec * fps)
    end_frame = int(end_time_sec * fps)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    for frame_num in range(start_frame, end_frame):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    print(f"✅ Saved segment from {start_time_sec}s to {end_time_sec}s → {output_path}")

# RUN:
split_video(
    input_path=r'C:\mary\OilDetectionProject\ToRunOn.mp4',  # your full video path
    output_path=r'C:\mary\OilDetectionProject\ToRunOn_segment.mp4',  # where to save the segment
    start_time_sec=73,  # 1:13 = 73 seconds
    end_time_sec=78     # 1:18 = 78 seconds
)
