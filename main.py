import string
import time
import pyautogui

print("""
    ░▒█░▒█░░█▀█░░█░░░▀░░█▀▄░█░▒█░█▀▀░░░▒█▀▀▀█░▄▀▀▄░█▀▀▄░█▀▄▀█░░░▒█▀▀▄░█░░░░█▀▀▄░▀█▀░░░▒█▀▀▄░▄▀▀▄░▀█▀
    ░▒█▀▀█░█▄▄█▄░█░░░█▀░█░░░█░▒█░▀▀▄░░░░▀▀▀▄▄░█▄▄█░█▄▄█░█░▀░█░░░▒█░░░░█▀▀█░█▄▄█░░█░░░░▒█▀▀▄░█░░█░░█░
    ░▒█░▒█░░░░█░░▀▀░▀▀▀░▀▀▀░░▀▀▀░▀▀▀░░░▒█▄▄▄█░█░░░░▀░░▀░▀░░▒▀░░░▒█▄▄▀░▀░░▀░▀░░▀░░▀░░░░▒█▄▄█░░▀▀░░░▀░

                -----------------------------------------------------------
                | Note : In Discord, Make Sure not to go over at 50 Time! |
                -----------------------------------------------------------
                |            Info : Created in 6/8/2023  10:52            |
                -----------------------------------------------------------
                |  Credits H4licus SpamChatBot : LagichMine               |
                |  Youtube : https://www.youtube.com/@lagichminecraft4652 |
                -----------------------------------------------------------
                !!            Remember, This is Only for Funny           !!
                -----------------------------------------------------------
""")
OP = int(input("Did you ready to spam? [1 = Yes] : "))
if OP == 1:
        spam = input("Enter The Word you want to Spam : ")
dem = int(input("""
    Note : In Discord, Make Sure not to go over at 50 Time!
    How Many Time do you want to Spam : """))
print("you have 10 second, Place your Cursor on the Chat Box where do you want Type!")
time.sleep(10)
for i in range(dem):
        pyautogui.typewrite(spam)
        pyautogui.press("enter")
        time.sleep(0.1)
print("Spammed" + spam + " " + dem + "Times!")

if OP == 1:
    exit
