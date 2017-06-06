#
#
#
#draw a circle by mouse

import pyautogui
import math
 
width, height = pyautogui.size()
 
r = 250  # 圆的半径
# 圆心
o_x = width/2
o_y = height/2
 
pi = 3.1415926
 
for i in range(10):   # 转10圈
	for angle in range(0, 360, 5):  # 利用圆的参数方程
		X = o_x + r * math.sin(angle*pi/180)
		Y = o_y + r * math.cos(angle*pi/180)
 
		pyautogui.moveTo(X, Y, duration=0.1)
