# google_search.py

"""
Description:
    Using Google Search to search for known vulnerabiltieis

Author:
    Nishant Krishna

Created:
    14 May, 2022
"""

from googlesearch import search
from sympy import Q


class GoogleSearch:
    def perform_google_search(self, host, query_string):
        """
        Perform google search using the host and query string.

        Args:
            host (string): Target system
            query_string (String): Query string
        """
        for query in search(host + " " + query_string, stop=5):
            print(query)


if __name__ == "__main__":
    google_search = GoogleSearch()
    google_search.perform_google_search(
        "site:<<Domain>>", 'inurl:"/wp-json/" -wordpress')
