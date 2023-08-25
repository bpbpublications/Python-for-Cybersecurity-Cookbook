# http_response_header_analysis_kali.py

"""
Description:
    Parse and prints the HTTP response header of the simulated phishing website using Kali Linux's SET.

Author:
    Nishant Krishna

Created:
    08 October, 2022
"""

import requests


class HttpResponseHeaderPrinter:
    def parse_response_header(self, url):
        response = requests.head(url)
        print(response.headers)


if __name__ == "__main__":
    response_header = HttpResponseHeaderPrinter()
    # The local site running on Kali Linux. Update it as per your setup
    print ('Response headers for phishing site:')
    response_header.parse_response_header('http://172.18.125.141/')

    print('\nResponse header for genuine site:')
    response_header.parse_response_header('https://www.facebook.com')
