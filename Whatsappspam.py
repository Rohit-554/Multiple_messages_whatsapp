import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")        # foraccessingwhatsappweb
time.sleep(30)                      # program will start to type after this seconds
for i in range(40):                 # number of times you want to send
    pyautogui.typewrite("kya bhosdike kal bata dega ans")         # your message
    # pyautogui.typewrite("You are Amazing")
    # pyautogui.typewrite("You are Awesome")
    pyautogui.press("enter")
