# nmap_detect_ciphers.py

"""
Description:
    Detect the cipher suites configured on the target system.


Author:
    Nishant Krishna

Created:
    5 June, 2022
"""

import nmap3
import json


class NmapCipherDetector:
    def detect_ciphers(self, host) -> None:
        """
        Detect the ciphers configured in the target system.

        Args:
            host (string): host to scan
        """
        nmap = nmap3.Nmap()

        # Use the nmap's version detection function to piggy back and detect the ciphers
        scan_results = nmap.nmap_os_detection(
            "host", args="--script ssl-enum-ciphers -p 443 " + host)
        print(json.dumps(scan_results, indent=4))


if __name__ == "__main__":
    cipher_detector = NmapCipherDetector()
    cipher_detector.detect_ciphers('<<host>')
