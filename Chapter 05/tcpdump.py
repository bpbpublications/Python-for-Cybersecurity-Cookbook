# tcpdump.py

"""
Description:
    Runs tcpdump as a subprocess and then prints the network captured.


Author:
    Nishant Krishna

Created:
    23 July, 2022
"""

import subprocess
import time


class TcpDump:
    def do_capture(self):
        # Use -l option for line buffered pipe so that we can print them as the output is generated. -c can be
        # used to limit the number of packets being captured
        tcpdump_subprocess = subprocess.Popen(('tcpdump', '-l', '-c 5'), stdout=subprocess.PIPE)

        # Print until the program is interrupted
        for output in iter(tcpdump_subprocess.stdout.readline, b''):
            print(output.rstrip())


if __name__ == "__main__":
    print('Capturing packets using tcpdump. Press Ctrl+C to stop...')
    time.sleep(1)
    tcpdump = TcpDump()
    tcpdump.do_capture()
