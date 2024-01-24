import pyautogui
import time

# Modules


user = input("Hi, Pls tell who is using (Sphnix or Symprax) : ")
if user == "Sphnix" or "sphnix":
    Sphnix_Choice = input("Code Bruv")
    if Sphnix_Choice == "Spotify":
        pyautogui.click(860, 1064)
        time.sleep(4)
        pyautogui.click(222, 449)
        time.sleep(2)
        pyautogui.click(482, 422)

if user == "Symprax" or "symprax":
    print("SID")
