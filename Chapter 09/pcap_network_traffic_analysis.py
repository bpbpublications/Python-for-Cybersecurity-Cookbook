# pcap_network_traffic_analysis.py

"""
Description:
    Uses pyshark to read the PCAP file and perform network traffic analysis of the captured network packets in the file.


Author:
    Nishant Krishna

Created:
    21 November, 2022
"""

import os
import pyshark

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class PcapNetworkTrafficAnalysis:
    def do_analysis(self):
        # Read a PCAP (Packet Capture) file and print the details
        pcap_file_name = os.path.join(__location__, 'output.pcap')

        # Apply filter for DNS packets
        # capture = pyshark.FileCapture(pcap_file_name, display_filter="dns")
        # for packet in capture:
        #     print(packet)

        # Apply filter for TCP packets on port 80
        capture = pyshark.FileCapture(pcap_file_name, display_filter="tcp.port == 80")
        for packet in capture:
            print (packet)


if __name__ == "__main__":
    pcap_traffic_analysis = PcapNetworkTrafficAnalysis()
    pcap_traffic_analysis.do_analysis()
