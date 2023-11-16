import os
import pyautogui
import time

def active(prog: str):
    os.system("wmic")
    time.sleep(10)
    pyautogui.write(f"product where name='{prog}' call uninstall")
