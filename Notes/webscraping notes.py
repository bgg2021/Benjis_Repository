# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/" # this is a nice website for scraping. Not all websites are like this.

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

# find data in my soup object
# by tagname
title = soup.findAll("title")  # returns a list of all tags called <title>
print(title)

# by attribute
fontsize = soup.findAll(style="font-size: 8px")
print(fontsize)

for fonts in fontsize:
    print(fonts.text)

# by css class

quotes = soup.findAll(class_="quote")
for quote in quotes:
    print(quote.text)

# by strings

einstein = soup.findAll(string="Albert Einstein")

for e in einstein:
    print(e)

# combine some of the above
quotes = soup.findAll("span", class_="text")
for quote in quotes:
    print(quote.text)

# find all authors

authors = soup.findAll("small", class_="author", itemprop="author")

for author in authors:
    print(author.text)

print(len(quotes), len(authors))

for i in range(len(quotes)):
    print(quotes[i])
    print("\t-", authors[i].text)