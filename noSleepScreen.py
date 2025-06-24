import pyautogui
import time

print("Prevent sleep with click started. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.click()  # perform a left-click at current mouse position
        time.sleep(30)     # wait 30 seconds
except KeyboardInterrupt:
    print("Prevent sleep script stopped.")
