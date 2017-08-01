# Song list downloader

### Required Libraries - 
	
	urllib	
	beautifulsoup
	winsound

### Usage :
	- Run the script
	- Input the number of songs
	- Enter the songs one by one
	- Songs are downloaded to the same folder

### Sample Input - 

	5
	Kygo It Ain't Me 
	Gryffin & Illenium ft. Daya - Feel Good
	Taylor Swift- We Are Never Ever Getting Back Together
	Alesso Years
	Adele- Rolling in the Deep

### How it works
	- Search youtube with the search_term = <SongName + 'lyrics'>
	- Get the first video link
	- Use this link in the youtubeinmp3 API to get the download link
	- Save the file
	
### ToDo
	Automatically download top 10 songs of the week at the end of the week.
	Do not download if its already present (Checked by hashing).
 
