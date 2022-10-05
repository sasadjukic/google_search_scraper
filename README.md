<strong>WARNING!</strong>
<br>
Google generally doesn't want you to scrape their engine. They may temporary block you if you perform too many searches this way. You may use VPN to avoid this
to happen  

<strong>SPECIAL THANKS</strong>
<br>
Logo for this program is made with much help fom this image https://www.onlygfx.com/magnifying-glass-clipart-png-transparent/

<strong>ABOUT THIS PROGRAM</strong>
<br><br>
Google Search Scraper is a simple program that scrapes google search engine and writes a csv file with all the data 
The program uses Python/Flask for backend, and HTML, CSS, vanilla JS for front end. BeautifulSoup is used to scrape data from Google.
The data is transfered from BE to FE via Flask-socketIO

<strong>HOW IT WORKS</strong>
<br>
1. User enters search term
2. The program submits the search term to Google search
3. Using BeautifulSoup the program scrapes the Google search for as many pages as indicated (2 by default but this can be any number you want)<br>
4. - (a) Using Flask-socketIO the program sends all the data for JavaScript to process and display it on the screen
   - (b) At the same time all the data from Google is sent to our write.py to file all the data in the CSV format
5. If user wants to perform more searches, they just click on the logo and go to the home page for a new search

<strong>WHY TO MAKE THIS PROGRAM?</strong>
<br>
1. I did it to practice sockets
2. You may want to collect and analyze Google data

<strong>FEATURES</strong>
1. This program allows you to modify how many pages you want to search (line 27 in run.py)
2. You can modify the timer of the for loop to slower the scraper to potentially avoid Google ban (line 40 in run.py)

<strong>SCREENSHOTS</strong>

