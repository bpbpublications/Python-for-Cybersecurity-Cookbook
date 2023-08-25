# wireshark_file_capture.py

"""
Description:
    Uses pyshark and Wireshark CLI Utility (tshark) to perform a live capture on an interface and save the content to a .pcap file.


Author:
    Nishant Krishna

Created:
    22 July, 2022
"""

import os
import pyshark

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class WiresharkFileCaputure:
    def do_capture(self):
        # Capture the packet into a PCAP (Packet Capture) file
        pcap_file_name = os.path.join(__location__, 'output.pcap')
        capture = pyshark.LiveCapture(interface='en0', output_file=pcap_file_name)
        capture.sniff(packet_count=10)


if __name__ == "__main__":
    wireshark_file_capture = WiresharkFileCaputure()
    wireshark_file_capture.do_capture()
