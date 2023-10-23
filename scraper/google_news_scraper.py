import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        xml = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(xml, parser)
        lista = []
        for item in sp.find_all("item"):
            title = item.find("title")
            if title:
                lista.append(title.text + "\n")
                print("\n" + title.text)
            continue
        with open("titulos.txt", "w") as file:
            file.writelines(lista)

site = "https://news.google.com/news/rss/headlines"
Scraper(site).scrape()
