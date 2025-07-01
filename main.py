from djitellopy import Tello
from oil_detection_listener import start_oil_detection_listener
from drone_scan import scan_room
from live_annotated_stream import start_annotated_stream
import threading
import time

def main():
    print("Initializing drone and oil detection system...")

    tello = Tello()
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    tello.streamon()
    print("Video stream active.")
    tello.streamon()
    time.sleep(5)  # wait for stream to stabilize

    #Get frame_reader once to avoid UDP conflicts
    frame_reader = tello.get_frame_read()

    # Wait until valid frame is available
    while frame_reader.frame is None or frame_reader.frame.size == 0:
        print("Waiting for frame...")
        time.sleep(0.1)
    frame = frame_reader.frame

    # Start live annotated stream
    threading.Thread(target=start_annotated_stream, args=(tello, frame_reader), daemon=True).start()
    time.sleep(2)  # Allow some time for the stream to start

    # Start oil detection listener (in parallel)
    listener_thread = threading.Thread(target=start_oil_detection_listener, args=(tello, frame_reader))
    listener_thread.start()


    # Start scanning movement (parallel)
    #scan_room(tello)

    # Wait for detection thread to finish
    listener_thread.join()

    print("Oil detection complete. Shutting down...")
    tello.streamoff()
    tello.end()



if __name__ == "__main__":
    main()
