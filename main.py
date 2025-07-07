from djitellopy import Tello
from oil_detection_listener import start_oil_detection_listener
from drone_scan import scan_room
from live_annotated_stream import start_annotated_stream
import threading
import time
from raw_live_stream import start_raw_stream  
import threading
from raw_video_saver import save_raw_video


def main():
    print("Initializing drone and oil detection system...")

    tello = Tello()
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    tello.streamon()
    print("Video stream active.")
    time.sleep(5)  # wait for stream to stabilize

    #Get frame_reader once to avoid UDP conflicts
    frame_reader = tello.get_frame_read()

    print("Waiting for first valid frame...")
    while True:
        frame = frame_reader.frame
        if frame is not None and frame.size > 0:
            break
        time.sleep(0.1)
    print("First frame received.")

    # Create a stop event for for communicating between threads
    stop_event = threading.Event()

    # Start raw stream instead of annotated stream
    #threading.Thread(target=start_raw_stream, args=(tello, frame_reader), daemon=True).start()

    # Start live annotated stream
    threading.Thread(target=start_annotated_stream, args=(tello, frame_reader), daemon=True).start()
    time.sleep(2)  # Allow some time for the stream to start

    # Start oil detection listener (in parallel), with stop_event to control it and handle race conditions
    listener_thread = threading.Thread(target=start_oil_detection_listener, args=(tello, frame_reader, stop_event))
    listener_thread.start()

    # Start raw video saver (in parallel)
    video_saver_thread = threading.Thread(target=save_raw_video, args=(tello, frame_reader))
    video_saver_thread.start()


    # Start scanning movement (parallel)
    scan_room(tello)
    # Signal the listener to stop
    #time.sleep(20)
    stop_event.set()

    # Wait for detection thread to finish
    listener_thread.join()

    print("Oil detection complete. Shutting down...")
    tello.streamoff()
    tello.end()



if __name__ == "__main__":
    main()
