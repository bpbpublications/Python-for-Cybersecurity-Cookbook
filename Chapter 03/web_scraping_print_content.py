# web_scraping_print_content.py

"""
Description:
    Print the content of a website using requests.get().


Author:
    Nishant Krishna

Created:
    5 June, 2022
"""

import requests


class WebScraping:
    def print_website_content(self, url) -> None:
        request = requests.get(url)
        print(request.content)


if __name__ == "__main__":
    web_scraping_content = WebScraping()
    web_scraping_content.print_website_content('https://www.google.com')
