import time

def scan_room(tello):
    print("Starting room scan...")

    tello.takeoff()
    time.sleep(2)

    tello.move_forward(5)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    tello.move_forward(5)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    tello.move_forward(5)
    time.sleep(1)

    tello.rotate_counter_clockwise(90)
    tello.move_forward(5)
    time.sleep(1)

    tello.land()
    print("Room scan complete.")
