from PIL.ImageOps import grayscale
import pyautogui
import time
import threading
import os
from pynput import keyboard

pyautogui.PAUSE = 0.01

ClickerEnabled = True
GoldClickerEnabled = True
BuyerEnabled = True

def SearchAndClick(file, confidenceValue):
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and GoldClickerEnabled:
            try:
                pos = pyautogui.locateCenterOnScreen(file, grayscale=True, confidence=confidenceValue)
                pyautogui.moveTo(pos.x, pos.y)
            except:
                pass
            time.sleep(5)

def AutoBuy():
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and BuyerEnabled:
            pyautogui.click(CW.width*0.85+CW.left, CW.height*0.1+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.86+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.8+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.74+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.68+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.62+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.56+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.5+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.44+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.38+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.32+CW.top)
            pyautogui.click(CW.width*0.91+CW.left, CW.height*0.26+CW.top)
            time.sleep(15)

def ClickTheCookie():
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and ClickerEnabled:
            pyautogui.click(CW.width*0.15+CW.left, CW.height*0.39+CW.top, clicks=10, interval=0.001, _pause=False)

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

searcher = threading.Thread(target=SearchAndClick, args=('goldCookie.png', .5))
userSearcher = threading.Thread(target=SearchAndClick, args=('goldCookie_user.png', .5))
clicker = threading.Thread(target=ClickTheCookie)
buyer = threading.Thread(target=AutoBuy)

searcher.start()
userSearcher.start()
clicker.start()
buyer.start()

with keyboard.GlobalHotKeys({
        '<esc>': Exit,
        '<ctrl>+<alt>+c': ToogleClicker,
        '<ctrl>+<alt>+с': ToogleClicker,
        '<ctrl>+<alt>+g': ToogleGoldClicker,
        '<ctrl>+<alt>+п': ToogleGoldClicker,
        '<ctrl>+<alt>+b': ToogleBuyer,
        '<ctrl>+<alt>+и': ToogleBuyer}) as h:
    h.join()