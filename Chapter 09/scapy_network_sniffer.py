# scapy_network_sniffer.py

"""
Description:
    Uses Scapy to perform network packet sniffing operations.


Author:
    Nishant Krishna

Created:
    22 November, 2022
"""

import scapy.all as scapy


class ScapyNetworkSniffer:
    def do_sniff(self):
        capture = scapy.sniff(iface='en0', count=5)
        print('\nCaptured packet summary:')
        print(capture.summary())

        print('\nCaptured packet details:')
        for packet in capture:
            print(packet.show())


if __name__ == "__main__":
    sniffer = ScapyNetworkSniffer()
    sniffer.do_sniff()
