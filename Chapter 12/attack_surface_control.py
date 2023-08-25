# attack_surface_control.py

"""
Description:
    This security controls shows how one can identify vulnerabilities and attack surface in a target system.

Author:
    Nishant Krishna

Created:
    20 February, 2023
"""

import nmap3
import json
import psutil
import subprocess


class AttackSurfaceControl:
    def check_open_ports(self):
        print('\nList of open ports: ')
        nmap = nmap3.Nmap()
        scan_results = nmap.scan_top_ports('127.0.0.1')
        print(json.dumps(scan_results, indent=4))

    def check_listening_sockets(self):
        print('\nList of open listening sockets: ')

        net_connections = psutil.net_connections()
        for conn in net_connections:
            if conn.status == psutil.CONN_LISTEN:
                print(conn)

    def list_members_privileged_groups(self):
        print('\nPrivileged users found on this system:')

        output = subprocess.check_output('members adm', shell=True)
        output_list = output.decode('utf-8').split('\n')
        print('Members in the group adm: ', output_list)

        output = subprocess.check_output('members sudo', shell=True)
        output_list = output.decode('utf-8').split('\n')
        print('Members in the group sudo: ', output_list)


if __name__ == "__main__":
    attack_surface = AttackSurfaceControl()
    attack_surface.check_open_ports()
    attack_surface.check_listening_sockets()
    attack_surface.list_members_privileged_groups()
