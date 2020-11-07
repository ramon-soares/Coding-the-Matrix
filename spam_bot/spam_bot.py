# !pip install pyautogui

import pyautogui as pg
import time

time.sleep(3)
arquivo = open("py_wiki", "r")
for palavra in arquivo:
    pg.typewrite(palavra)
    pg.press("enter")
    time.sleep(0.25)
