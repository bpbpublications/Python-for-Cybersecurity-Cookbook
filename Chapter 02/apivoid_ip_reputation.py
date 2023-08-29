# apivoid_ip_reputation.py

"""
Description:
    Check the IP Reputation of an IP address using APIVoid "iprep" API.

Author:
    Nishant Krishna

Created:
    16 May, 2022
"""

import requests
import json

apivoid_key = "<<API Key>>"


class ApivoidIpReputation:
    def apivoid_query(self, endpoint, ip_address) -> json:
        """
        A generic method to query APIVoid using the endpoint supplied

        Args:
            endpoint (string): API endpoint
            ip_address (string): IP Address

        Returns:
            json: Query output
        """
        try:
            r = requests.get(url='https://endpoint.apivoid.com/'+endpoint +
                             '/v1/pay-as-you-go/?key='+apivoid_key+'&ip='+ip_address)
            return json.loads(r.content.decode())
        except:
            return {}


if __name__ == "__main__":
    apivoid_ip_reputation = ApivoidIpReputation()
    json_data = apivoid_ip_reputation.apivoid_query('iprep', '<<IP Address>')
    print(json.dumps(json_data, indent=4))
