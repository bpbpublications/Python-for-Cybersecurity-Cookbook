# log_monitor.py

"""
Description:
    Monitor logs as they are generated and take actions based on the content of the log.

Author:
    Nishant Krishna

Created:
    14 February, 2023
"""


import tailer
import os
import re

# Set the location of the file to read from the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class LogMonitor:
    def monitor_log(self, log_file):
        log_filename = os.path.join(__location__, log_file)

        for log_line in tailer.follow(open(log_filename)):
            print(log_line)

            pattern = re.compile('error', re.IGNORECASE)
            matches = pattern.search(log_line)

            if matches:
                print('Error found in log')


if __name__ == "__main__":
    monitor = LogMonitor()
    monitor.monitor_log('log_file.log')
