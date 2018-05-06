import pyautogui
import time

while True:
	x, y = pyautogui.position()
	print(str(x),str(y))
	time.sleep(0.5)
