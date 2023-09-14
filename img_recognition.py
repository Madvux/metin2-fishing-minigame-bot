from pyautogui import locateOnScreen
from pydirectinput import press
from time import sleep
from random import uniform

is_working = False

def do_this(x):
    sleep(uniform(0.1, 0.3))
    for _ in range(x):
        sleep(uniform(0.08, 0.12))
        print("I can see " + str(x))
        press('space', duration=uniform(0.06,0.1))
    sleep(uniform(6.9, 7.3))
    print("---------------------------")

while 1:
    sleep(0.1)
    is_working = True
    for i in range(1,6):
        if locateOnScreen('img/{}.png'.format(i), region=(470,250,150,150), confidence=0.8) != None:
            do_this(i)
            is_working = False

    if is_working != True:
        press('1', duration=uniform(0.06,0.1))
        sleep(uniform(0.6, 0.9))
        press('space', duration=uniform(0.06,0.1))
