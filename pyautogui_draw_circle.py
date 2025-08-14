#
#
#
#draw a circle by mouse

import math
import pyautogui

width, height = pyautogui.size()

r = 250  # radius
# Center point
o_x = width / 2
o_y = height / 2

for _ in range(10):  # draw circle 10 times
    for angle in range(0, 361, 5):  # 360 degrees inclusive
        radians = math.radians(angle)
        X = o_x + r * math.sin(radians)
        Y = o_y + r * math.cos(radians)

        pyautogui.moveTo(X, Y, duration=0.1)
