# interpret_protocol_header.py

"""
Description:
    Uses pyshark and Wireshark CLI Utility (tshark) to perform a capture on an interface and then shows the fields of the 'ip' protocol header so that we can interpret them.

Author:
    Nishant Krishna

Created:
    20 August, 2022
"""

import pyshark


class ProtocolHeaderInterpreter:
    def do_capture(self):
        # Change the interface to what's configured on your host. Generally it is 'eth0'. On macOS it can be 'en0'.
        capture = pyshark.LiveCapture(interface='en0')
        # Capture 5 packets
        capture.sniff(packet_count=5)

        # Print the 'ip' layer of the packet
        print('\n\n---- Printing only \'ip\' layer of the packet')
        print(capture[0].ip)

        print('\n\n---- Printing all the fields of the \'ip\' layer the packet')
        print(capture[0].ip.field_names)


if __name__ == "__main__":
    header_interpreter = ProtocolHeaderInterpreter()
    header_interpreter.do_capture()
