import time, pyautogui
from datetime import datetime


def screenshot():

    d_t = datetime.now() #Get the current date and time for the screenshot name, save it in a variable
    name = '{}.png'.format(d_t) # use an in-line format string to create the date and time naming variable
    time.sleep(1) #wait X amount of seconds before screen capture
    img = pyautogui.screenshot( name) #use the name variable and attach a file format
    img.show() #preview the image

screenshot() # call the function
