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

     # Start live annotated stream
    threading.Thread(target=start_annotated_stream, args=(tello,), daemon=True).start()
    time.sleep(2)  # Allow some time for the stream to start

    # Start oil detection listener
    listener_thread = threading.Thread(target=start_oil_detection_listener, args=(tello,))
    listener_thread.start()

    # Start scanning movement (parallel)
    scan_room(tello)

    # Wait for detection thread to finish
    listener_thread.join()

    print("Oil detection complete. Shutting down...")
    tello.streamoff()
    tello.end()



if __name__ == "__main__":
    main()
