from PIL.ImageOps import grayscale
import pyautogui
import time
import multiprocessing
import os
import random
from pynput import keyboard

pyautogui.PAUSE = 0.001
searcher = multiprocessing.Process()
clicker = multiprocessing.Process()
buyer = multiprocessing.Process()

def SearchAndClick():
    CW = pyautogui.getActiveWindow()
    if CW is not None and "Cookie Clicker" in CW.title:
        pos = pyautogui.locateOnScreen('goldCookie.png', grayscale=True, confidence=0.5)
        if pos is not None:
            pos = pyautogui.center(pos)
            pyautogui.click(pos.x, pos.y)
        pos = pyautogui.locateOnScreen('goldCookie_user.png', grayscale=True, confidence=0.5)
        if pos is not None:
            pos = pyautogui.center(pos)
            pyautogui.click(pos.x, pos.y)

def SearchAndClickService():
    global searcher
    while True:
        if searcher.is_alive():
            searcher.terminate()
        time.sleep(1)
        searcher = multiprocessing.Process(target=SearchAndClick)
        searcher.start()
        time.sleep(3)

def AutoBuy():
    while True:
        CW = pyautogui.getActiveWindow()
        if CW is not None and "Cookie Clicker" in CW.title:
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
        if CW is not None and "Cookie Clicker" in CW.title:
            x = CW.width*0.155+CW.left
            y = CW.height*0.42+CW.top
            pyautogui.click(x, y)
        else:
            time.sleep(1)

def ToogleClicker():
    global clicker
    if clicker.is_alive():
        clicker.terminate()
    else:
        clicker = multiprocessing.Process(target=ClickTheCookie)
        clicker.start()

def ToogleSearcher():
    global searcher
    if searcher.is_alive():
        searcher.terminate()
    else:
        searcher = multiprocessing.Process(target=SearchAndClickService)
        searcher.start()

def ToogleBuyer():
    global buyer
    if buyer.is_alive():
        buyer.terminate()
    else:
        buyer = multiprocessing.Process(target=AutoBuy)
        buyer.start()

def Exit():
    searcher.terminate()
    clicker.terminate()
    buyer.terminate()
    os._exit(0)

if __name__ == '__main__':
    ToogleClicker()
    ToogleSearcher()
    ToogleBuyer()
    with keyboard.GlobalHotKeys({
            '<esc>': Exit,
            '<ctrl>+<alt>+c': ToogleClicker,
            '<ctrl>+<alt>+с': ToogleClicker,
            '<ctrl>+<alt>+g': ToogleSearcher,
            '<ctrl>+<alt>+п': ToogleSearcher,
            '<ctrl>+<alt>+b': ToogleBuyer,
            '<ctrl>+<alt>+и': ToogleBuyer}) as h:
        h.join()