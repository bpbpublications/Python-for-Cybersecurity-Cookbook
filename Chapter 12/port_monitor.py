# port_monitor.py

"""
Description:
    Monitor few ports and check if they are open.

Author:
    Nishant Krishna

Created:
    12 February, 2023
"""


import psutil


class PortMonitor:
    def check_config(self):
        FTP_PORT1 = 20
        FTP_PORT2 = 21

        ftp_port1_open = ftp_port2_open = False

        for connection in psutil.net_connections():
            if connection.laddr[1] == FTP_PORT1:
                ftp_port1_open = True

            if connection.laddr[1] == FTP_PORT2:
                ftp_port2_open = True

        if (ftp_port1_open == True or ftp_port2_open == True):
            print('FTP port found open')
        else:
            print('FTP port found closed')


if __name__ == "__main__":
    monitor = PortMonitor()
    monitor.check_config()
