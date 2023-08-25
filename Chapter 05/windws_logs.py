# windows_logs.py

"""
Description:
    Print specic logs from Windows Security Log to a file which can then be analysed later.

Author:
    Nishant Krishna

Created:
    01 August, 2022
"""

import platform
import win32evtlog
import win32evtlogutil


class WindowsLogs:
    def get_scurity_logs(self):
        if (platform.system != 'Windows'):
            handle = win32evtlog.OpenEventLog(None, "Security")
            flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ

            # Check how many records we are able to read
            security_records = (handle, flags, 0)
            print('Found ', len(security_records), ' records')

            # This will print the first record but we won't be able to make out any details inside the log
            if len(security_records) > 0:
                print(security_records[0])

            # Now read all the logs
            all_logs = win32evtlog.ReadEventLog(handle, flags, 0)

            # Get log message of all the logs which can now be read by us
            for event_log in all_logs:
                log_message = win32evtlogutil.SafeFormatMessage(event_log, 'Security')
                print(log_message)
        else:
            print('This program can only be run on Windows')


if __name__ == "__main__":
    logs = WindowsLogs()
    logs.get_scurity_logs()
