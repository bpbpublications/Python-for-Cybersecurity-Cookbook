# apivoid_domain_reputation.py

"""
Description:
    Check the Domain Reputation of a host using APIVoid "domainbl" API.

Author:
    Nishant Krishna

Created:
    16 May, 2022
"""

import requests
import json

apivoid_key = "<<API Key>>"


class ApivoidDomainReputation:
    def apivoid_query(self, endpoint, host) -> json:
        """
        A generic method to query APIVoid using the endpoint supplied

        Args:
            endpoint (string): API endpoint
            host (string): host

        Returns:
            json: Query output
        """
        try:
            r = requests.get(url='https://endpoint.apivoid.com/'+endpoint +
                             '/v1/pay-as-you-go/?key='+apivoid_key+'&host='+host)
            return json.loads(r.content.decode())
        except:
            return {}


if __name__ == "__main__":
    apivoid_domain_reputation = ApivoidDomainReputation()
    json_data = apivoid_domain_reputation.apivoid_query('domainbl', '<<Host>>')
    print(json.dumps(json_data, indent=4))
