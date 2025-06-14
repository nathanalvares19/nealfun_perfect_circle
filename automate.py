import pyautogui
import time
import math

# === SETTINGS ===
# ( All coordinates taken relative to top left of the entire screen )

center_x = 960    # X coordinate of center of circle
center_y = 602    # Y coordinate of center of circle
radius = 455      # Change radius
steps = 4   # Increase to smoothen circle

# Open https://neal.fun/perfect-circle/
print("Switch to the browser and click 'GO'. Starting in 5 seconds...")
time.sleep(3)

# Move to starting point (Rightmost point of the circle)
start_x = center_x + radius
start_y = center_y 
pyautogui.moveTo(start_x, start_y)
pyautogui.mouseDown()

# Draw the circle
for i in range(steps + 1):
    angle = 2 * math.pi * i / steps
    print(math.degrees(angle))
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pyautogui.moveTo(x, y, duration=0.1)      # Add duration=time parameter to modify drawing speed
    
pyautogui.mouseUp()

print("Done! Check your score.")
