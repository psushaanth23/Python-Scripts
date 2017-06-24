'''
Alerts you by making a beep sound when the cricket match has been resumed play after rain.

Author : Sushaanth P

Usage- 
- Run the program when a cricket match is halted due to rain.
- Continue other important works.
- The program will alert you once the match is resumed.

'''

import requests
import winsound
from time import sleep

#adjust these for tweaking the sound
BeepTime = 1
BeepInterval = 1
freq = 6
noOfTimes = 10

count = 0 

def generateSound(noOfTimes):
	while noOfTimes:
		winsound.Beep(freq*100,BeepTime*1000)
		sleep(BeepInterval)
		noOfTimes-=1

while(1):
	response = requests.get('http://cricbuzz.com/')
	count+=1

	print('Number of times checked: '+str(count))
	index = str(response.content).find('cb-ovr-flo')
	CheckHere = str(response.content)[index:index+100]

	if CheckHere.find('Play stopped due to rain')==-1:
		print('>>>>>>>>>>>> Match is resumed <<<<<<<<<<<<<')
		generateSound(noOfTimes)
		break

	sleep(10)
