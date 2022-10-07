import pyautogui
import time

pyautogui.click(155, 750, button='left')
pyautogui.write("paint")
pyautogui.press("enter")
time.sleep(5)

distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, button='left')
    distance -= 20
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, button='left')
    distance -= 20
    pyautogui.dragRel(0, -distance, button='left')
    
time.sleep(2)