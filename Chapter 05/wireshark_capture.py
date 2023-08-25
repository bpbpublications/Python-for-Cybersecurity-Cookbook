# wireshark_capture.py

"""
Description:
    Uses pyshark and Wireshark CLI Utility (tshark) to perform a capture on an interface.


Author:
    Nishant Krishna

Created:
    22 July, 2022
"""

import pyshark


class WiresharkCaputure:
    def do_capture(self):
        # Change the interface to what's configured on your host. Generally it is 'eth0'. On macOS it can be 'en0'.
        capture = pyshark.LiveCapture(interface='en0')
        # Capture 5 packets
        capture.sniff(packet_count=5)
        print(capture)
        print(capture[0])


if __name__ == "__main__":
    wireshark_capture = WiresharkCaputure()
    wireshark_capture.do_capture()
