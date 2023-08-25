# windows_firewall_check.py

"""
Description:
    Get details about Windows firewall.


Author:
    Nishant Krishna

Created:
    14 January, 2023
"""

import windows_tools.windows_firewall as windows_firewall
import subprocess


class WindowsFirewall:
    def check_windows_firewall(self):
        # Use windows_tools to check the firewall status
        firewall_active = windows_firewall.is_firewall_active()
        print('Windows firewall status:', firewall_active)

        if firewall_active == True:
            # Use netsh command through subprocess to get details about all the profiles
            print(subprocess.check_call('netsh advfirewall show allprofiles'))
        else:
            print('Windows firewall not active...')


if __name__ == "__main__":
    firewall = WindowsFirewall()
    firewall.check_windows_firewall()
