# kismet_client.py

"""
Description:
    Connect with Kismet server and get the details.

Author:
    Nishant Krishna

Created:
    20 February, 2023
"""

import kismet_rest


class KismetClient:
    def get_device_list(self):
        client = kismet_rest.KismetConnector(username='nishant', password='test@123')
        devices = client.device_list();
        print(devices)


if __name__ == "__main__":
    kismet = KismetClient()
    kismet.get_device_list()
