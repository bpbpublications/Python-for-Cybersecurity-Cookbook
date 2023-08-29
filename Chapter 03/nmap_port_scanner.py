# nmap_port_scanner.py

"""
Description:
    Scan for all the open ports using python3-nmap.


Author:
    Nishant Krishna

Created:
    5 June, 2022
"""

import nmap3
import json


class NmapPortScanner:
    def port_scan(self, host) -> None:
        """
        Scan the top ports.

        Args:
            host (string): host to scan
        """
        nmap = nmap3.Nmap()

        # Perform nmap's top ports scan. By default the number is set to 10 which can be increased adding a
        # parameter "default=<number", where <number> is the number of top ports you want to scan
        scan_results = nmap.scan_top_ports(host)

        print(json.dumps(scan_results, indent=4))


if __name__ == "__main__":
    nmap_scanner = NmapPortScanner()
    nmap_scanner.port_scan('<<host>')
