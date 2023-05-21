import pyautogui
import pytesseract
import time
import random

n1 = pyautogui.locateAllOnScreen("source1.png",confidence=0.98)
n2 = pyautogui.locateAllOnScreen("source2.png",confidence=0.98)
n3 = pyautogui.locateAllOnScreen("source3.png",confidence=0.98)
n4 = pyautogui.locateAllOnScreen("source4.png",confidence=0.98)
n1 = list(n1)
n2 = list(n2)
n3 = list(n3)
n4 = list(n4)
print(n1)
print(n2)
print(n3)
print(n4)
n1_center = pyautogui.center(n1[0])
n2_center = pyautogui.center(n2[0])
n3_center = pyautogui.center(n3[0])
n4_center = pyautogui.center(n4[0])
num = [n1_center,n2_center,n3_center,n4_center]
randomnum = random.choice(num)
pyautogui.click(n1)
pyautogui.moveTo(200, 200)