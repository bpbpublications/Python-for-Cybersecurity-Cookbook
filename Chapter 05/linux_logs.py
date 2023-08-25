# linux_logs.py

"""
Description:
    Print Linux logs into files which can then be analysed later.


Author:
    Nishant Krishna

Created:
    01 August, 2022
"""

import os
import platform


class LinuxLogs:
    def get_linux_logs(self):
        # The commands are different based on the OS. Darwin means its macOS system
        if platform.system() == 'Linux':
            os.system('last > last.log')
            os.system('cat /var/log/secure | grep \"Failed password\" | tail -100 > secure_logs.txt')
        elif platform.system() == 'Darwin':
            os.system('last > last.log')
        else:
            print('This program only be run on Linux or macOS')


if __name__ == "__main__":
    logs = LinuxLogs()
    logs.get_linux_logs()
