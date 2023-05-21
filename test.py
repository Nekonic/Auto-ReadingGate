from cgitb import text
import pyautogui
import pytesseract
import time
import random
import cv2
import os
try:
    from PIL import Image
except ImportError:
    import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
Q = []

trueA = []
falseA = []

trueQA = [Q, trueA]
falseQA = [Q, falseA]

for i in range(20):
    #Q
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('RgateQ.png', region=(650, 580, 1635, 110))

    image = cv2.imread("RgateQ.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    textQ = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    #A1
    cv2.waitKey(0)

    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('Rgate1.png', region=(750, 770, 1450, 130))

    image = cv2.imread("Rgate1.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text1 = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    cv2.waitKey(0)

    #A2
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('Rgate2.png', region=(750, 930, 1450, 130))

    image = cv2.imread("Rgate2.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text2 = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    cv2.waitKey(0)

    #A3
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('Rgate3.png', region=(750, 1130, 1450, 130))

    image = cv2.imread("Rgate3.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text3 = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    cv2.waitKey(0)

    #A4
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('Rgate4.png', region=(750, 1320, 1450, 130))

    image = cv2.imread("Rgate4.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text4 = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    cv2.waitKey(0)

    #click
    n1 = pyautogui.locateAllOnScreen("source1.png", confidence=0.98)
    n2 = pyautogui.locateAllOnScreen("source2.png", confidence=0.98)
    n3 = pyautogui.locateAllOnScreen("source3.png", confidence=0.98)
    n4 = pyautogui.locateAllOnScreen("source4.png", confidence=0.98)
    n1 = list(n1)
    n2 = list(n2)
    n3 = list(n3)
    n4 = list(n4)
    n1_center = pyautogui.center(n1[0])
    n2_center = pyautogui.center(n2[0])
    n3_center = pyautogui.center(n3[0])
    n4_center = pyautogui.center(n4[0])
    n_center = [n1_center, n2_center, n3_center, n4_center]
    x = random.randrange(0,3)
    pyautogui.click(n_center[x])
    pyautogui.moveTo(200, 200)


    #True or False
    textA = [text1, text2, text3, text4]
    while 1:
        true = pyautogui.locateAllOnScreen("true.png", confidence=0.98)
        false = pyautogui.locateAllOnScreen("false.png", confidence=0.98)
        true = list(true)
        false = list(false)
        if len(true) != 0:
            print("Q. ", textQ, "\nA ", x, ".", textA[x], "\n", "is true")
            print()
            Q.append(textQ)
            trueA.append(textA)
            break
        else:
            print("Q. ", textQ, "\nA ", x, ".", textA[x], "is false")
            print()
            Q.append(textQ)
            falseA.append(textA)
            break

print()
print("is trueQA")
for a in range(len(trueQA)):
    print(a," is true")

print()
print("is falseQA")
for a in range(len(falseQA)):
    print(a," is true")

