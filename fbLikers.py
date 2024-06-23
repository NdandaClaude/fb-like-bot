import pyautogui
import time


like_button_position = (550, 980)  
heart_button_position = (600, 980)


def send_like():
    pyautogui.click(like_button_position)
    time.sleep(1)  


def send_heart():
    pyautogui.click(heart_button_position)
    time.sleep(1) 


while True:
    send_like()
    send_heart()


