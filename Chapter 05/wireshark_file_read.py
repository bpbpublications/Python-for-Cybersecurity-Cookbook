# wireshark_file_read.py

"""
Description:
    Uses pyshark to read the PCAP file and print the details.


Author:
    Nishant Krishna

Created:
    23 July, 2022
"""

import os
import pyshark

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class WiresharkFileRead:
    def do_capture(self):
        # Read a PCAP (Packet Capture) file and print the details
        pcap_file_name = os.path.join(__location__, 'output.pcap')
        capture = pyshark.FileCapture(pcap_file_name)
        print(capture[0])


if __name__ == "__main__":
    wireshark_file_read = WiresharkFileRead()
    wireshark_file_read.do_capture()
