'''input
5

Snow Patrol- Chasing Cars
Beyonce- Irreplacable
2007:
Fergie- Big Girls Don't Cry
Avril Lavigne- Girlfriend
Rihanna - Umbrella
Sean Kingston- Beautiful Girls
Alicia Keys- No One
Timbaland (ft. OneRepublic)-  Apologize
Silverchair- Straight Lines
2008:
Flo Rida- Low
Leona Lewis- Bleeding Love
Jordin Sparks (ft.Chris Brown) - No Air
Sara Bareilles- Love Song
Katy Perry- I Kissed a Girl
Rihanna- Distubria
Pink- So What
Jason Mraz- I'm Yours
2009:
The Black Eyed Peas- Boom Boom Pow
Lady Gaga- Poker Face
Lady Gaga (ft. Colby O'Donis) Just Dance
Taylor Swift- Love Story
Beyonce- Single Ladies
The Black Eyed Peas- I Gotta Feeling
Katy Perry- Hot n Cold
2010:
Kesha- Tik Tok
Katy Perry (ft. Snoop Dog) - California Girls
Usher (Will.i.Am)- OMG
BoB. (ft. Hayley Williams) - Airplanes
Eminem (ft. Rihanna) - Love The Way You Lie
Lady Gaga- Bad Romance
Jay-Z & Alicia Keys- Empire State of Mind
Justin Bieber- Baby
2011:
Adele- Rolling in the Deep
Katy Perry- Firework
LMFAO (ft. Lauren Bennett, Goonrock)- Party Rock Anthem
Katy Perry (ft. Kanye West) - ET
Pitbull- Give Me Everything
Bruno Mars- Grenade
Nicki Minaj- Superbass
2012:
Gotye (ft. Kimbra)- Somebody That I Used To Know
Carly Rae Jepson- Call Me Maybe
fun. - We Are Young
One Direction- What Makes You Beautiful
Maroon 5 (ft. Wiz Khalifa)- Payphone
Kelly Clarkson- Stronger
Psy- Gangnam Style
Rihanna (ft. Calvin Harris) - We Found Love
2013:
Baauer- Harlem Shake
Taylor Swift- We Are Never Ever Getting Back Together
Macklemore (ft. Ryan lewis)- Thrift shop
Rihanna (ft. Mikky Ekko) Stay
Pink Nate Reuss-  Just Give Me a Reason
Taylor Swift- I Knew You Were Trouble
Justin Timberlake- Mirrors
Robin Thicke (ft. T.I, Pharrell)- Blurred Lines

'''
import urllib
import urllib.request as urllib2
from bs4 import BeautifulSoup


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
	if(song.find('200')==-1):
		print('>>> Downloading Song : \t'+song)
		download(song)
		print('>>> '+(str(i+1))+' down '+str(n-i-1)+' to go\t\t'+song+' is Done\n')
			