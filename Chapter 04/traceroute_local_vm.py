# traceroute_local_vm.py

"""
Description:
    Implements 'traceroute' functionality in Python to check for the route to a host.


Author:
    Nishant Krishna

Created:
    06 July, 2022
"""

from icmplib import traceroute


class TracerouteLocalVM:
    def check_traceroute(self, host) -> None:

        # hops will now store all the hops from the current host to the remote host. By default, max_hops is 30
        # if no max_hops=<value> is supplied
        print ('Checking hops for the host...')
        hops = traceroute(host, max_hops=20)
        print('All Hops:\n', hops, '\n')

        print('Distance/TTL \tAddress \tAverage round-trip time  \tPackets Sent')
        last_distance = 0

        for hop in hops:
            if last_distance + 1 != hop.distance:
                print('No response from gateway')

            # See the Hop class for details
            print(
                f'{hop.distance:<15} {hop.address:<15} {hop.avg_rtt} ms \t\t\t{hop.packets_sent:<5}')

            last_distance = hop.distance


if __name__ == "__main__":
    traceroute_check = TracerouteLocalVM()

    # Check Traceroute for the IP Addresses of the local VMs. Replace with your IP Address
    traceroute_check.check_traceroute('172.25.120.171')
    traceroute_check.check_traceroute('172.25.115.189')
