# live_raw_stream.py

import cv2
import time

def start_raw_stream(tello, frame_reader, max_duration=30):
    print("Starting raw Tello video stream...")

    try:
        cv2.namedWindow("Tello Raw Stream", cv2.WINDOW_NORMAL)
        cv2.moveWindow("Tello Raw Stream", 100, 100)

        start_time = time.time()

        while True:
            frame = frame_reader.frame
            if frame is None or frame.size == 0:
                print("[Raw Stream] Waiting for valid frame...")
                time.sleep(0.05)
                continue

            cv2.imshow("Tello Raw Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("User pressed 'q'. Exiting...")
                break

            if time.time() - start_time > max_duration:
                print(f"Stream duration reached ({max_duration}s). Exiting...")
                break

            time.sleep(0.03)

    except Exception as e:
        print(f"[Raw Stream Error] {e}")

    finally:
        cv2.destroyAllWindows()
        print("Raw Tello stream stopped.")
