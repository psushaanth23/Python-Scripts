# Resumed Play Notifier

Alerts you by making a beep sound when the cricket match has resumed play after rain.
Afterall who wants to keep refreshing the web and wasting time when python can do that for us. :P

### Usage

	- Run the program when a cricket match is stopped due to rain.
	- Continue other important works.
	- The program will alert you once the match is resumed.

### How it works
	
	- The program keeps refreshing the cricbuzz page every 10 secs.
	- If it sees that match is resumed in the current match area of the page.
		- Then alert the user.
	- Else
		- Repeat the steps again.
