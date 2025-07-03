# frame_annotator.py

import cv2
import torch

def annotate_frame_with_boxes(frame, detections, class_names=None, color=(0, 255, 0), thickness=2):
    """
    Draw bounding boxes and labels with confidence on the given frame.

    Args:
        frame (np.ndarray): Original image/frame.
        detections (torch.Tensor or np.ndarray): YOLO detections.
        class_names (list): List of class names (optional).
        color (tuple): Box color.
        thickness (int): Line thickness.

    Returns:
        np.ndarray: Annotated frame.
    """
    if isinstance(detections, torch.Tensor):
        detections = detections.cpu().numpy()

    for det in detections:
        if len(det) >= 6:
            x1, y1, x2, y2, conf, cls = det[:6]
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            label = f"{int(cls)}"
            if class_names and int(cls) < len(class_names):
                label = class_names[int(cls)]
            text = f"{label} {conf * 100:.1f}%"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame
