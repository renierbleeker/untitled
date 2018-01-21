from bs4 import BeautifulSoup
import requests
import pprint
import re
import pyperclip

urls = ['https://www.jouwictvacature.nl/vacatures/java', 'https://www.jouwictvacature.nl/vacatures/net']
#scrape elements
for url in urls:
    response = requests.get(url)
    page_soup = BeautifulSoup(response.content, "html.parser")

    containers = page_soup.findAll("article", {"class": "vacancy-item item up"})

    for container in containers:

        # Company name
        company_container = container.div.h2
        company = company_container.text.strip()

        # Title
        title_container = container.findAll("div", {"class": "info"})
        title = title_container[0].img["alt"]

        print(company, title)

    #print titles only
    #h1 = soup.find("h1", class_= "class-headline")
    #print(h1.get_text())