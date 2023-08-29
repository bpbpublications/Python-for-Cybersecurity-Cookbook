# http_response_header_interpret.py

"""
Description:
    Interprets the HTTP response header in terms of the vulnerabilities.

Author:
    Nishant Krishna

Created:
    17 August, 2022
"""

import requests


class HttpResponseHeaderInterpreter:
    def parse_response_header(self, url):
        response = requests.head(url)
        print (response.headers)

        # Interpret two of the headers

        try:
            x_frame_options = response.headers['X-Frame-Options']
            print('\nX-Frame-Options: ', x_frame_options)
            if ('DENY' in x_frame_options.upper() or 'SAMEORIGIN' in x_frame_options.upper()):
                print('Value of X-Frame-Options OK')
            else:
                print('Either X-Frame-Options not set or \"DENY\" / \"SAMEORIGIN\" not found in X-Frame-Options. Changing the value to \"DENY\" / \"SAMEORIGIN\" recommended')
        except:
            print('Either X-Frame-Options not set or \"DENY\" / \"SAMEORIGIN\" not found in X-Frame-Options. Changing the value to \"DENY\" / \"SAMEORIGIN\" recommended')

        try:
            x_content_type = response.headers['X-Content-Type-Options']
            print('\nX-Content-Type-Options: ', x_content_type)
            if ('nosniff' in x_content_type.lower()):
                print('Value of X-Content-Type-Options OK')
            else:
                print('Either X-Content-Type-Options not set or \"nosniff\" not found in X-Content-Type-Options. Changing the value to \"nosniff\" recommended')
        except:
            print('Either X-Content-Type-Options not set or \"nosniff\" not found in X-Content-Type-Options. Changing the value to \"nosniff\" recommended')


if __name__ == "__main__":
    response_header = HttpResponseHeaderInterpreter()
    response_header.parse_response_header('<<Host>>')
