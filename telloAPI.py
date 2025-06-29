from djitellopy import Tello

# Create a Tello object
tello = Tello()

# Connect to the drone
tello.connect()
print(f"Battery: {tello.get_battery()}%")

# Take off
tello.takeoff()

# Fly forward 50 cm
tello.move_forward(50)


# Rotate clockwise 90 degrees
tello.rotate_clockwise(90)

# Land
tello.land()

# End connection (optional cleanup)
tello.end()
