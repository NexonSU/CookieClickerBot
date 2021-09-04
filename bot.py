from PIL.ImageOps import grayscale
import pyautogui
import time
import multiprocessing
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
        time.sleep(2.5)

def AutoBuy():
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and BuyerEnabled:
            pyautogui.click(CW.width+CW.left-550, CW.top+200)
            time.sleep(0.1)
            ltx = CW.width+CW.left-550
            lty = CW.top+400
            rbx = CW.width+CW.left-300
            rby = CW.height+CW.top
            ClickColorInRegion(ltx, lty, rbx, rby, 102, 255, 102)
        time.sleep(15)

def ClickColorInRegion(ltx, lty, rbx, rby, r, g, b):
    s = pyautogui.screenshot(region=(ltx, lty, rbx, rby))
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == (r, g, b):
                pyautogui.click(ltx+x, lty+y)
                return

def ClickTheCookie():
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and ClickerEnabled:
            pyautogui.click(CW.width*0.15+CW.left, CW.height*0.39+CW.top, clicks=5, interval=0.001, _pause=False)
        else:
            time.sleep(1)

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

if __name__ == '__main__':
    searcher = multiprocessing.Process(target=SearchAndClick, args=('goldCookie.png', .5))
    userSearcher = multiprocessing.Process(target=SearchAndClick, args=('goldCookie_user.png', .5))
    clicker = multiprocessing.Process(target=ClickTheCookie)
    buyer = multiprocessing.Process(target=AutoBuy)

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