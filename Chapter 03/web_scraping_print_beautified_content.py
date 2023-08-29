# web_scraping_print_beautified_content.py

"""
Description:
    Get the content of a website using requests.get() and then use BeautifulSoup to print the content which is readable.

    More information - https://www.crummy.com/software/BeautifulSoup/bs4/doc/


Author:
    Nishant Krishna

Created:
    5 June, 2022
"""

from bs4 import BeautifulSoup
import requests


class WebScraping:
    def print_beautified_website_content(self, url) -> None:
        request = requests.get(url)

        soup = BeautifulSoup(request.content, 'html5lib')
        print(soup.prettify())


if __name__ == "__main__":
    web_scraping_content = WebScraping()
    web_scraping_content.print_beautified_website_content(
        'https://www.google.com')
