# Mission-to-Mars

## Overview 

For this project, I was tasked with building a web application that would scrape Mars data from multiple websites using BeautifulSoup and Splinter. Then, I had to store the scraped data on a Mongo database, in which I would then use a Flask app to output the scraped data and images into a local HTML page. 

First, I had to set up an executable path and initialize Splinter, which essentially automates my Chrome web browser that allows me to visit and interact with, for example, clicking through web pages to retrieve certain pieces of information from the website. The web driver manager package was useful because it allowed me to use a driver to scrape websites without having to download and install a stand alone ChromeDriver, which can be a complicated process. 

MongoDB was used preferentially over SQL, because the data I was scraping from each website was not going to be uniform, nor would it be in the format that is best suited for SQL, for example, tabular and relational data. Mongo is better suited for this project because it will store the data that was scraped and then allow me to access it later as a document instead. 

Finally, I created an index.html file, which would allow me to create various tags to present the data/images on my HTML page using my own customizations. Every webpage is built using HTML, and have the same basic structure, for example, each element of a page is wrapped in a tag, and each tag is specific to the element it is holding. This is why it is so important to learn HTML, because it can be a powerful tool when trying to set up, create, edit, or reformat a webpage.

## Resources 

* Bootstrap 3
* Flask App
* Anaconda (Jupyter Notebook, Pandas, Python 3.9.12)
* VS Code 
* MongoDB/Mongosh
* ChromeDriver 
* Beautiful Soup
* Splinter & Selenium 
* Scraping Websites: 
  * 'https://redplanetscience.com/'
  * 'https://spaceimages-mars.com/'
  * 'https://galaxyfacts-mars.com/'
  * 'https://marshemispheres.com/'


## Results

The final webpage for a desktop webpage is shown below, (Fig. A). 

Fig A


Finally, I had to make sure that my webpage was also going to be responsive on a mobile or tablet. To do this, I had to look at the bootstrap grid documentation and add extra code in the class that I set my grid breakpoints for the desktop page, but instead I had to add a similar code that would work on mobile and tablets, as well, for example, 'col-xs-4'.
 
One issue that was bugging me was when I was looking at the mobile responsive version in DevTools, I noticed that the table was not fitting entirely into the frame, part of the table was cut off, and one could easily scroll over, but I thought it would look nicer if they didn't have to. So, I looked up more documentation and realized that if I added 'table-responsive table-condensed' into my scraping.py mars_facts definition, then that would fix the problem. Then, I checked how it would look on two different phones, a Samsung Galaxy S8 (Fig. B), and an Iphone 12 Pro (Fig. C), which are shown below. 

pic of mobile responsive on two different phones 


