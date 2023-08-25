# parse_protocol_headers.py

"""
Description:
    Uses pyshark and Wireshark CLI Utility (tshark) to perform a capture on an interface and then shows which headers were found in the capture.

Author:
    Nishant Krishna

Created:
    20 August, 2022
"""

import pyshark


class ProtocolHeaderParser:
    def do_capture(self):
        # Change the interface to what's configured on your host. Generally it is 'eth0'. On macOS it can be 'en0'.
        capture = pyshark.LiveCapture(interface='en0')
        # Capture 5 packets
        capture.sniff(packet_count=5)

        # Print all the layers of the packet
        print('---- Printing all the layers of the packet')
        print(capture[0])

        print('\n\n---- Printing all the layer names of the packet')
        print(capture[0].layers)

        # Print the 'ip' layer of the packet
        print('\n\n---- Printing only \'ip\' layer of the packet')
        print(capture[0].ip)

        print('\n\n---- Printing specific attributes of the packet')
        print(capture[0].transport_layer)

        print('\n\n---- Printing specific attributes of the \'ip\' layer the packet')
        print(capture[0].ip.src)
        print(capture[0].ip.dst)


if __name__ == "__main__":
    header_parser = ProtocolHeaderParser()
    header_parser.do_capture()
