# main.py

from see_from_tello import video, tello
from oil_detection_listener import start_oil_detection_listener

def main():
    print("Initializing drone and oil detection system...")
    
    # Tello and video are already initialized on import
    print("Video stream active.")
    
    # Start detection listener
    start_oil_detection_listener(video, tello)

if __name__ == "__main__":
    main()
