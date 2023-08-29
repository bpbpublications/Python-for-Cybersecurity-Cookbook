# dig_info.py

"""
Description:
    Get "dig" details for a host.

Author:
    Nishant Krishna

Created:
    05 May, 2022
"""

import pydig as pd


class DigInfo:
    def print_dig_info(self, host, type):
        """
            host: Host that you want the see the dig details for.
            type: Can be A, NS, CNAME, etc.
        """
        dig_info = pd.query(host, type)
        print(dig_info)


if __name__ == "__main__":
    dig_info = DigInfo()
    # Print A and NS (DNS servers) records
    dig_info.print_dig_info('google.com', 'A')
    dig_info.print_dig_info('google.com', 'NS')
