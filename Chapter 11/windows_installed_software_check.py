# windows_installed_software_check.py

"""
Description:
    Get details about the software installed on Windows sytem.


Author:
    Nishant Krishna

Created:
    16 January, 2023
"""

import wmi


class WindowsInstalledSoftware:
    def check_windows_installed_antivirus(self):
        wmi_ref = wmi.WMI()

        # Get details of software with 'windows' in it
        for software in wmi_ref.Win32_Product():
            if 'windows' in str(software.Name).lower():
                print(software)


if __name__ == "__main__":
    installed_software = WindowsInstalledSoftware()
    installed_software.check_windows_installed_antivirus()
