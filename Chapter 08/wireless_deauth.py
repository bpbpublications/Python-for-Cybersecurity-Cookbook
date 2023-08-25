# wireless_deauth.py

"""
Description:
    Scans for all the available wireless targets and performs deauthentication on the chosen interface.


Author:
    Nishant Krishna

Created:
    04 November, 2022
"""

import asyncio

from pyrcrack import AirodumpNg, AirmonNg
from rich.console import Console


class WiressDeauthentication:
    airmon_ng = AirmonNg()

    async def get_wlan_interface(self):
        for interface in await self.airmon_ng.interfaces:
            wlan_interface = interface.asdict()
            print('WLAN interface details: ', wlan_interface)
            print('WLAN interface name: ', wlan_interface['interface'])

    async def scan_for_wireless_targets(self):
        # Create a console where we will print the details
        console = Console()

        # Enable monitor mode and dump the scanned packet
        async with self.airmon_ng('wlan0') as wlan_mon:
            async with AirodumpNg() as packet_dump:
                async for scan_result in packet_dump(wlan_mon.monitor_interface):
                    console.print(scan_result.table)
                    await asyncio.sleep(10)


if __name__ == "__main__":
    wireless_deauthentication = WiressDeauthentication()
    asyncio.run(wireless_deauthentication.get_wlan_interface())
    asyncio.run(wireless_deauthentication.scan_for_wireless_targets())
