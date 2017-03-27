import webbrowser
import time
import os

url=input("Enter URL:")
refresh=input("enter refresh time in seconds:")
browser=input("Enter your browser:")
count=input("How many viws do you want:")

def openURL():
	os.system("TASKKILL /F /IM " + browser + ".exe")
	webbrowser.open(url)
	time.sleep(int(refresh))

	for i in range(int(count)):
		print("Webpage has been viewed")
		openURL()

openURL()
