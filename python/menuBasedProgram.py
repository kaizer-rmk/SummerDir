import os
import pyttsx3
from time import sleep

while(1):
	getCMD = input("Chat with me about your requirment: ")

	if ("run" in getCMD) and ("chrome"in getCMD):
		os.system("chrome")
		os.system("cls")
	elif (("run" in getCMD) or ("execute" in getCMD)) and (("notepad" in getCMD) or ("editor" in getCMD)):
		os.system("notepad")
		os.system("cls")
	elif ("break" in getCMD) or ("exit" in getCMD):
		break
	else:
		print("Cannot Find the Command")
		sleep(5)
		os.system("cls")

