import pyautogui
import time
import threading
import os
from pynput import keyboard

ClickerEnabled = True
GoldClickerEnabled = True
BuyerEnabled = True

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
        if type(curwintitle) == str and "Cookie Clicker" in curwintitle and ClickerEnabled:
            pyautogui.click(600, 850, clicks=10, interval=0.001)

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