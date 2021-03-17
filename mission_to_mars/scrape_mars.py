from splinter import Browser
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import os
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    #scrape mars news
    url = "http://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='rollover_description_inner')[0].text

    # Close the browser after scraping
    browser.quit()

    #scrape feautred image
    browser = init_browser()
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
    #click on Full Image link
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # #set up browser and beautiful soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #delay the code by two seconds
    time.sleep(2)

    #scrape the code to find the image
    featured_images = soup.find('img', class_='fancybox-image')
    url = featured_images['src']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + url

    # Close the browser after scraping
    browser.quit()

    #scrape mars facts
    #use Pandas read_url to read table
    browser = init_browser()
    url = 'https://space-facts.com/mars/'
    time.sleep(1)
    mars_table = pd.read_html(url)
    mars_df = mars_table[0]
    #convert to html table string
    html_mars_table = mars_df.to_html(classes = "data table", index=False, header = False, border=0)
    # #Close the browser after scraping
    browser.quit()

    # #scrape hemisphere images/title
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    #create an empty list to hold values
    hemisphere_image_urls = []

    #loop through hemisphere pages
    for i in range (4):
        hemisphere_dict = {}
        browser.links.find_by_partial_text('Hemisphere Enhanced')[i].click()

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        time.sleep(1)

        title = soup.find('h2', class_ = 'title').text
        image = soup.find('div', class_ = 'downloads')
        original_img = image('li')[0]
        url = original_img('a')
        image_url = url[0]['href']
        hemisphere_dict["title"] = title
        hemisphere_dict["image_url"] = image_url
        hemisphere_image_urls.append(hemisphere_dict)

        browser.back()

    # # Close the browser after scraping
    browser.quit()

    #store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": html_mars_table,
        "hemisphere_data": hemisphere_image_urls
    }

    browser.quit()
    # Return results
    return mars_data
