#This script saves the image of the region (left, top, width, height)) as savedimage.png in the path "C:\Users\Tomek\Downloads\Image-Recognition-Botting-Tutorial-master\Image-Recognition-Botting-Tutorial-master"

import pyautogui

im1 = pyautogui.screenshot(region=(450,250,150,150))
im1.save(r"./savedimage.png")
