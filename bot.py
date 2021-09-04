import pyautogui
import time
import threading

def SearchAndClick(file, confidenceValue):
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle:
            try:
                pos = pyautogui.locateCenterOnScreen(file, confidence=confidenceValue)
                pyautogui.click(pos.x, pos.y)
            except:
                pass
            time.sleep(0.25)

def AutoBuy():
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle:
            pyautogui.click(3500, 1850)
            pyautogui.click(3500, 1730)
            pyautogui.click(3500, 1600)
            pyautogui.click(3500, 1470)
            pyautogui.click(3500, 1350)
            pyautogui.click(3500, 1220)
            pyautogui.click(3500, 1100)
            pyautogui.click(3500, 960)
            pyautogui.click(3500, 830)
            pyautogui.click(3500, 700)
            pyautogui.click(3500, 570)
            pyautogui.click(3500, 450)
            pyautogui.click(3270, 220)
            time.sleep(15)

def ClickTheCookie():
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle:
            pyautogui.click(600, 850, clicks=10, interval=0.001)

searcher = threading.Thread(target=SearchAndClick, args=('goldCookie3.png', 0.9))
clicker = threading.Thread(target=ClickTheCookie)
buyer = threading.Thread(target=AutoBuy)

searcher.start()
clicker.start()
buyer.start()

clicker.join()