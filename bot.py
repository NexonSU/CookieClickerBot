from PIL.ImageOps import grayscale
import pyautogui
import time
import multiprocessing
import os
from pynput import keyboard

pyautogui.PAUSE = 0.01
ClickerEnabled = multiprocessing.Value('i', True)
GoldClickerEnabled = multiprocessing.Value('i', True)
BuyerEnabled = multiprocessing.Value('i', True)

def SearchAndClick(file, confidenceValue, Enabled):
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and Enabled.value:
            try:
                pos = pyautogui.locateCenterOnScreen(file, grayscale=True, confidence=confidenceValue)
                pyautogui.moveTo(pos.x, pos.y)
            except:
                pass
        time.sleep(2.5)

def AutoBuy(Enabled):
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and Enabled.value:
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

def ClickTheCookie(Enabled):
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title and Enabled.value:
            pyautogui.click(CW.width*0.15+CW.left, CW.height*0.39+CW.top, clicks=5, interval=0.001, _pause=False)
        else:
            time.sleep(1)

def ToogleClicker():
    if ClickerEnabled.value:
        ClickerEnabled.value = False
    else:
        ClickerEnabled.value = True

def ToogleGoldClicker():
    if GoldClickerEnabled.value:
        GoldClickerEnabled.value = False
    else:
        GoldClickerEnabled.value = True

def ToogleBuyer():
    if BuyerEnabled.value:
        BuyerEnabled.value = False
    else:
        BuyerEnabled.value = True

def Exit():
    searcher.terminate()
    userSearcher.terminate()
    clicker.terminate()
    buyer.terminate()
    os._exit(0)

if __name__ == '__main__':
    searcher = multiprocessing.Process(target=SearchAndClick, args=('goldCookie.png', .5, GoldClickerEnabled))
    userSearcher = multiprocessing.Process(target=SearchAndClick, args=('goldCookie_user.png', .5, GoldClickerEnabled))
    clicker = multiprocessing.Process(target=ClickTheCookie, args=(ClickerEnabled,))
    buyer = multiprocessing.Process(target=AutoBuy, args=(BuyerEnabled,))

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