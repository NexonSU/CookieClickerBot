import pyautogui
import time
import threading
import os
from pynput import keyboard

pyautogui.PAUSE = 0.01

ClickerEnabled = True
GoldClickerEnabled = True
BuyerEnabled = True

ScreenWidth = pyautogui.size().width
ScreenHeight = pyautogui.size().height

def SearchAndClick(file, confidenceValue):
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle and GoldClickerEnabled:
            try:
                pos = pyautogui.locateCenterOnScreen(file, confidence=confidenceValue)
                pyautogui.click(pos.x, pos.y)
            except:
                pass
            time.sleep(0.25)

def AutoBuy():
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle and BuyerEnabled:
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.86)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.8)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.74)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.68)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.62)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.56)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.5)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.44)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.38)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.32)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.26)
            pyautogui.click(ScreenWidth*0.91, ScreenHeight*0.2)
            pyautogui.click(ScreenWidth*0.85, ScreenHeight*0.1)
            time.sleep(15)

def ClickTheCookie():
    while True:
        curwintitle = pyautogui.getActiveWindowTitle()
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle and ClickerEnabled:
            pyautogui.click(ScreenWidth*0.15, ScreenHeight*0.39, clicks=10, interval=0.001)

def ToogleClicker():
    global ClickerEnabled
    if ClickerEnabled:
        ClickerEnabled = False
    else:
        ClickerEnabled = True

def ToogleGoldClicker():
    global GoldClickerEnabled
    if GoldClickerEnabled:
        GoldClickerEnabled = False
    else:
        GoldClickerEnabled = True

def ToogleBuyer():
    global BuyerEnabled
    if BuyerEnabled:
        BuyerEnabled = False
    else:
        BuyerEnabled = True

def Exit():
    os._exit(0)

searcher = threading.Thread(target=SearchAndClick, args=('goldCookie3.png', 0.9))
clicker = threading.Thread(target=ClickTheCookie)
buyer = threading.Thread(target=AutoBuy)

searcher.start()
clicker.start()
buyer.start()

with keyboard.GlobalHotKeys({
        '<esc>': Exit,
        '<ctrl>+<alt>+c': ToogleClicker,
        '<ctrl>+<alt>+g': ToogleGoldClicker,
        '<ctrl>+<alt>+b': ToogleBuyer}) as h:
    h.join()