# ping_connectivity_with_admin_previleges.py

"""
Description:
    Checks connectivity of a host using ICMP Ping.

    This program needs to be run as "administrator" or with "sudo" privileges, otherwise it will fail with
    an error similar to "PermissionError: [Errno 1] Operation not permitted". A user without privilege
    escalation can't send ICMP message and hence the error.


Author:
    Nishant Krishna

Created:
    31 May, 2022
"""

from pythonping import ping


class PingConnectivity:
    def check_ping_connectivity(self, host) -> None:
        ping(host, verbose=True)


if __name__ == "__main__":
    ping_check_connectivity = PingConnectivity()
    ping_check_connectivity.check_ping_connectivity('google.com')
