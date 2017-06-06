#
#
#
#get mouse position, use ctrl c to exit


import pyautogui
try:
    while True:
        x, y = pyautogui.position()
        print(x,y)
except KeyboardInterrupt:
    print('\nExit.')
