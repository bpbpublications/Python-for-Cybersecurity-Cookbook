# active_recon_tool.py

"""
Description:
    This is an example of how we can use published source code to create new Cybersecurity tools


Author:
    Nishant Krishna

Created:
    11 December, 2022
"""

import nmap3
import json
from icmplib import traceroute
import os
import platform


class ActiveReconTool:
    def check_ping_connectivity(self, host):
        # The commands line arguments are different based on the OS
        if platform.system() == 'Windows':
            status = os.system('ping ' + host + ' -n 1')
        else:
            status = os.system('ping -c 1 ' + host)

        return status

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

    def check_traceroute(self, host) -> None:
        # hops will now store all the hops from the current host to the remote host. By default, max_hops is 30
        # if no max_hops=<value> is supplied
        print('Checking hops for the host...')
        hops = traceroute(host, max_hops=20)
        print('All Hops:\n', hops, '\n')

        print('Distance/TTL \tAddress \tAverage round-trip time  \tPackets Sent')
        last_distance = 0

        for hop in hops:
            if last_distance + 1 != hop.distance:
                print('No response from gateway')

            # See the Hop class for details
            print(f'{hop.distance:<15} {hop.address:<15} {hop.avg_rtt} ms \t\t\t{hop.packets_sent:<5}')

            last_distance = hop.distance


if __name__ == "__main__":
    recon = ActiveReconTool()
    host = 'trustyfi.com'

    print('Checking connectivity:\n')
    status = recon.check_ping_connectivity(host)

    if status == 0:
        print('\nHost is Up.  Continuing with other operations...')

        print('\nChecking Traceroute:\n')
        recon.check_traceroute(host)

        print('\nPerforming port scan:\n')
        recon.port_scan(host)
    else:
        print('\nHost is Down. Cannot continue with other operations...')
