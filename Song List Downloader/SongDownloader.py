'''
Download any song
Author : Sushaanth P

Sample Input - 

5
Kygo It Ain't Me 
Gryffin & Illenium ft. Daya - Feel Good
Taylor Swift- We Are Never Ever Getting Back Together
Alesso Years
Adele- Rolling in the Deep

'''


import urllib
import urllib.request as urllib2
from bs4 import BeautifulSoup
import winsound

def save(link, SaveAs):
	urllib2.urlretrieve(link, SaveAs)


def getLink(url, search, attr):
	query = urllib.parse.quote(search)
	response = urllib2.urlopen(url + query)
	soup = BeautifulSoup(response.read(),"lxml")
	for vid in soup.findAll(attrs={'class':attr})[0:1]:
		return vid['href'] 

def download(SongName):
	SongToSearch = SongName+' lyrics'

	#get the video link from youtube
	getURL = "https://www.youtube.com/results?search_query="
	attr = 'yt-uix-tile-link'
	div = getLink(getURL, SongToSearch, attr)
	songLink = 'https://www.youtube.com' + div

	#get the download link using the video link
	getURL = "https://www.youtubeinmp3.com/download/?video="
	attr = 'button'
	div = getLink(getURL, songLink, attr)
	downloadLink = 'https://www.youtubeinmp3.com'+div

	save(downloadLink, SongName+'.mp3')

n = int(input())

for i in range(n):
	song = input()
	print('>>> Downloading Song : \t'+song)
	try:
		download(song)
		print('>>> '+(str(i+1))+' down '+str(n-i-1)+' to go\t\t'+song+' is Done\n')
	except:
		print('Exception : I guess you need to check the internet connection')


print('ALL SONGS ARE DOWNLOADED')
winsound.Beep(2000,4000)
