# wireless_sniff.py

"""
Description:
    A simple wireless traffic sniffer in debug mode

Author:
    Nishant Krishna

Created:
    08 November, 2022
"""

import pyshark
import json


class WirelessSniffer:
    def do_sniff(self):
        # Change the interface to what's configured on your host
        capture = pyshark.LiveCapture(interface='en0', debug=True)
        capture.sniff(timeout=5)
        print('\n', capture, '\n')

        # Print one packet
        print(capture[0])


if __name__ == "__main__":
    sniffer = WirelessSniffer()
    sniffer.do_sniff()
