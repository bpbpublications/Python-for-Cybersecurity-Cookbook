# censys_print_host_details.py

"""
Description:
    Use Censys to get all the public information about a target system.

Author:
    Nishant Krishna

Chapter:
    Chapter 02 - Passive Reconnaissance

Created:
    15 May, 2022
"""

import json
from censys.search import CensysHosts

censys_host = CensysHosts()


class CensysHostDetails:
    def print_host_details(self, ip_address) -> json:
        try:
            ipinfo = censys_host.view(ip_address)
        except:
            ipinfo = {}

        print(json.dumps(ipinfo, indent=4))


if __name__ == "__main__":
    censys_info = CensysHostDetails()
    censys_info.print_host_details('<<IP Address>>')
