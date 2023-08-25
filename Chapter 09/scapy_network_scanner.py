# scapy_network_scanner.py

"""
Description:
    Uses Scapy to perform basic reconnaissance operations on the network.


Author:
    Nishant Krishna

Created:
    22 November, 2022
"""

import scapy.all as scapy


class ScapyNetworkScanner:
    def do_arp(self):
        """
        Perform ARP operation
        """
        print('\nPerform ARP operation:')
        operation = scapy.ARP()
        print(operation.summary())
        print(operation.show())

    def do_ls(self):
        """
        List the layers and fields which can be set for a ARP packet  
        """
        print('\nPerform LS operation:')
        operation = scapy.ARP()
        print(scapy.ls(operation))

    def list_interfaces(self):
        """
        List all the network interfaces on the local host  
        """
        print('\nList interfaces:')
        print(scapy.get_if_list())

    def list_routes(self):
        """
        List all the network routes on the local host  
        """
        print('\nList routes:')
        print(scapy.conf.route)


if __name__ == "__main__":
    scanner = ScapyNetworkScanner()
    scanner.do_arp()
    scanner.do_ls()
    scanner.list_interfaces()
    scanner.list_routes()
