# crawling_print_all_links.py

"""
Description:
    Print all the links on a web page using BeautifulSoup.

    More information - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

    Though BeautifulSoup is a very powerful module, and takes care of most of the crawling needs, it is worth looking at urllib. Many very good examples of urllibs can be found at https://docs.python.org/3/howto/urllib2.html.


Author:
    Nishant Krishna

Created:
    5 June, 2022
"""

from bs4 import BeautifulSoup
import requests


class WebCrawler:
    def print_beautified_website_content(self, url) -> None:
        request = requests.get(url)

        soup = BeautifulSoup(request.content, 'html5lib')

        for link in soup.find_all('a'):
            print(link.get('href'))


if __name__ == "__main__":
    web_crawler = WebCrawler()
    web_crawler.print_beautified_website_content('https://www.google.com')
