# ping_connectivity_os_command.py

"""
Description:
    Checks connectivity of a host using the OS "ping" command.


Author:
    Nishant Krishna

Created:
    31 May, 2022
"""

import os
import platform


class PingConnectivityOS:
    def check_ping_connectivity(self, host):
        # The commands line arguments are different based on the OS
        if platform.system() == 'Windows':
            status = os.system('ping ' + host + ' -n 1')
        else:
            status = os.system('ping -c 1 ' + host)

        return status


if __name__ == "__main__":
    ping_check_connectivity = PingConnectivityOS()
    status = ping_check_connectivity.check_ping_connectivity('google.com')

    if status == 0:
        print("Host is up")
    else:
        print("Host is down")
