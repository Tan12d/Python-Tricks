import pyautogui
import time
import random

time.sleep(5)

pyautogui.moveTo(100,100,duration=1)

for _ in range(50):
    x = random.randint(100,400)
    y = random.randint(130,900)

    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()

pyautogui.moveTo(800,800,duration=1)