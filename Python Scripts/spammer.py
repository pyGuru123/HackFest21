import pyautogui
import pyperclip

string = input("Enter the spam msg ")
count = int(input("Enter the no of Count"))

def spam():
	pyperclip.copy(string)
	pyautogui.moveTo(738,691)
	pyautogui.click()
	pyautogui.hotkey('ctrl','v')
	pyautogui.hotkey('enter')
	pyautogui.click()

for i in range(count):
	spam()

