# nmap_vulners.py

"""
Description:
    Use NMAP NSE to check for vulnerabilities.


Author:
    Nishant Krishna

Created:
    31 July, 2023
"""

import subprocess


class NmapVulners:
    def scan_target(self, target):
        output = subprocess.check_output('nmap -sV --script vulners --script-args mincvss=5.0 ' + target, shell=True)
        out_list = output.decode('utf-8').split('\n')
        print('Vulnerabilities found on this system:\n', out_list)


if __name__ == "__main__":
    vulners = NmapVulners()
    vulners.scan_target("192.168.19.132")
