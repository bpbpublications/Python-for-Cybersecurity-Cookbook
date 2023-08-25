# wireshark_live_capture_wireless_interface.py

"""
Description:
    Uses pyshark and Wireshark CLI Utility (tshark) to perform a live capture on a wireless interface.


Author:
    Nishant Krishna

Created:
    01 November, 2022
"""

import time
import pyshark


class WiresharkLiveCaputure:
    def do_capture(self):
        # Change the interface to what's configured on your host
        capture = pyshark.LiveCapture(interface='en0')

        # Continuously sniff next 10 packets every 1 second and show them as they are captured
        for packet in capture.sniff_continuously(packet_count=10):
            print(packet)
            time.sleep (1)


if __name__ == "__main__":
    wireshark_live_capture = WiresharkLiveCaputure()
    wireshark_live_capture.do_capture()
