# google_dorks.py

"""
Description:
    Using Pagodo to get vulnerabilities/exploit information for a host using Google Dorks.

    Look at https://github.com/opsdisk/pagodo for more details. Available under GPL License.

Author:
    Nishant Krishna

Created:
    14 May, 2022
"""

from pagodo.pagodo import Pagodo


class GoogleDorks:
    def process_dorks(self):
        # Set various keys for Pagodo. Be careful not to set the minimum_delay_between_dork_searches_in_seconds and maximum_delay_between_dork_searches_in_seconds keys to a small number when performing a large number of Dorks serches as Google may ban your IP address
        pg = Pagodo(
            google_dorks_file="Chapter 02/dorks.txt",
            domain="<<Domain>>",
            max_search_result_urls_to_return_per_dork=3,
            save_pagodo_results_to_json_file=True,
            minimum_delay_between_dork_searches_in_seconds=10,
            maximum_delay_between_dork_searches_in_seconds=15,
            save_urls_to_file=True,
            verbosity=4
        )

        pagodo_results_dict = pg.go()

        for key, value in pagodo_results_dict["dorks"].items():
            print(f"dork: {key}")
            for url in value["urls"]:
                print(url)


if __name__ == "__main__":
    google_dorks = GoogleDorks()
    google_dorks.process_dorks()
