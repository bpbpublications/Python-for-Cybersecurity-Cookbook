# login_failed_control.py

"""
Description:
    A security control to check for login failed using /var/log/auth.log

Author:
    Nishant Krishna

Created:
    14 February, 2023
"""


import tailer
import re


class LogMonitor:
    def monitor_log(self, log_file):
        counter = 0

        for log_line in tailer.follow(open(log_file)):
            print(log_line)

            pattern = re.compile('authentication failure', re.IGNORECASE)
            matches = pattern.search(log_line)

            if matches:
                # We need to get the last token and split again
                log_tokens = log_line.split(' ')
                user_token = log_tokens[-1]
                user = user_token.split('=')
                user_name = user[-1]

                counter += 1
                print('Authentication failure for user: ', user_name, ', Count: ', counter)


if __name__ == "__main__":
    monitor = LogMonitor()
    monitor.monitor_log('/var/log/auth.log')
