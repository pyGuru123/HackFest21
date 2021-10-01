# visit pyGuru on YouTube
# pip install pillow
# pip install keyboard

from PIL import ImageGrab
import keyboard


def screenShot():
	sc = ImageGrab.grab() 
	sc.save('screenshot.png')

while True:
	if keyboard.is_pressed('p'):
		screenShot()
		break