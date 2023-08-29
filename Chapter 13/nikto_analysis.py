# nikto_analysis.py

"""
Description:
    Demonstrates how to crack password using John The Ripper from Python


Author:
    Nishant Krishna

Created:
    13 June, 2023
"""

import os


class NiktoScanner:
    def scan_target(self, target):
        os.system("nikto -host " + target)


if __name__ == "__main__":
    nikto = NiktoScanner()
    nikto.scan_target("192.168.19.132")
