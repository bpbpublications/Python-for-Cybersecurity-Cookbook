# apivoid_dns_lookup.py

"""
Description:
    Perform DNS records lookup for a host using APIVoid "dnslookup" API.

Author:
    Nishant Krishna

Created:
    16 May, 2022
"""

import requests
import json

apivoid_key = "<<API Key>>"


class ApivoidDnsLookup:
    def apivoid_query(self, endpoint, host, action) -> json:
        """
        A generic method to query APIVoid using the endpoint supplied

        Args:
            endpoint (string): API endpoint
            host (string): host
            action (string): Action like 'dna-a', 'dns-aaaa', 'dns-mx', 'dns-ns', 'dns-dmarc', 'dns-ptr' (reverse DNS), 'dns-txt', 'dns-any' (all records), 'dns-cname', 'dns-soa', 'dns-srv', and 'dns-caa'

        Returns:
            json: Query output
        """
        try:
            r = requests.get(url='https://endpoint.apivoid.com/'+endpoint +
                             '/v1/pay-as-you-go/?key='+apivoid_key+'&host='+host+"&action="+action)
            return json.loads(r.content.decode())
        except:
            return {}


if __name__ == "__main__":
    apivoid_dns_lookup = ApivoidDnsLookup()
    json_data = apivoid_dns_lookup.apivoid_query(
        'dnslookup', '<<Host>>', 'dns-a')
    print(json.dumps(json_data, indent=4))
