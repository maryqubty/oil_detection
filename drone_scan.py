import time

def scan_room(tello):
    print("Starting room scan...")

    tello.takeoff()
    time.sleep(2)

    tello.move_forward(400)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    time.sleep(1)

    tello.move_forward(150)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    time.sleep(1)
    
    tello.move_forward(400)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    time.sleep(1)

    tello.move_forward(150)
    time.sleep(1)

    tello.land()
    print("Room scan complete.")
