# netstat.py

"""
Description:
    Implements 'netstat' functionalty in Python to check details about ports and services.


Author:
    Nishant Krishna

Created:
    31 May, 2022
"""

# We are using net_connection from psutils to check for all the 'netstat' functionality. psutil has a hugh collection
# of very useful utiliy functions which are worth exploring.
from psutil import net_connections


class NetStats:
    def print_net_connections(self) -> None:
        print('TCP connections:')
        print(net_connections(kind='tcp'))
        print('\n')
        print('UDP connections:')
        print(net_connections(kind='udp'))


if __name__ == "__main__":
    netstats = NetStats()
    netstats.print_net_connections()
