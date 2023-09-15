import pyautogui as spam 
import time

limite_msg = input("quantas msg? ")
msg = input("qual a msg?")

i = 0

time.sleep(10)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

    i+=1