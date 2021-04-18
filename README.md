# web-scraping-challenge

**Background**

For this project, I was tasked with building a web application that scrapes various websites for data related to the Mission to Mars and display it on a single HTML webpage.

![](https://github.com/erinmann12/web-scraping-challenge/blob/main/mission_to_mars/images/top_page.PNG)

**Tools Used**

1. Jupyter Notebook
2. Pandas
3. Beautiful Soup
4. Requests/Splinter
5. MongoDB 
6. Flask
7. HTML

**Project Tasks**

In part one, I completed scraped a variety of websites using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. I first scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the most recent news title and paragraph text and assigned them to variables. Next, I accessed the [JPL Featured Space Image](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html) and used splinter to navigate the site and find the URL, which I set to a variable. 

![](https://github.com/erinmann12/web-scraping-challenge/blob/main/mission_to_mars/images/beautifulsoup.PNG)

I then visited the [Mars Facts webpage](https://space-facts.com/mars/) and used Pandas to scrape the table with information about Mars. I then converted the data to an HTML table string. Finally, I visited the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images of each of Mars' hemispheres. I used Requests/Splinter to click on each link and find the URL and title of the hemisphere. I appended the information of each hemisphere to a dictionary and created a list of the dictionaries.

![](https://github.com/erinmann12/web-scraping-challenge/blob/main/mission_to_mars/images/dictionary.PNG)

In part two, I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped in part one.

-------------------------------------------------------------------------------------------------------------------------------------------------

Erin Mann

erin.mann2019@gmail.com

