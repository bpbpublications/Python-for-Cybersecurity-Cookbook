# http_response_header_print.py

"""
Description:
    Parse and prints the HTTP response header of a website

Author:
    Nishant Krishna

Created:
    17 August, 2022
"""

import requests

class HttpResponseHeaderPrinter:
    def parse_response_header(self, url):
        response = requests.head(url)
        # Print all the headers
        print(response.headers)

        # Print specific headers
        print('\nSet-Cookie: ', response.headers['Set-Cookie'])
        print('X-Frame-Options: ', response.headers['X-Frame-Options'])
        print('X-Content-Type-Options: ', response.headers['X-Content-Type-Options'])
        print('Referrer-Policy: ', response.headers['Referrer-Policy'])


if __name__ == "__main__":
    response_header = HttpResponseHeaderPrinter()
    response_header.parse_response_header('<<Host>>')
