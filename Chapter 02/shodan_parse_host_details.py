# shodan_print_host_details.py

"""
Description:
    Use Shodan to get all the public information about a target system and then parse few keys/attributes.

Author:
    Nishant Krishna

Created:
    15 May, 2022
"""

from shodan import Shodan
import json

api = Shodan('<<API Key>>')


class ShodanHostDetailsParser:
    def parse_host_details(self, ip_address):
        """""
        Print details about the IP address

        Args:
            ip_address (String): IP address to scan
        """
        ipinfo = api.host(ip_address)

        # First convert the response to JSON using json.dumps and then load it in a JSON object
        json_data = json.loads(json.dumps(ipinfo))

        # Now print the attributes we need. The get() function can be used to get specific attributes
        print('city: ', json_data.get('city'))
        print('latitude: ', json_data.get('latitude'))
        print('longitude: ', json_data.get('longitude'))
        print('country_name: ', json_data.get('country_name'))


if __name__ == "__main__":
    shodan_host_details_parser = ShodanHostDetailsParser()
    shodan_host_details_parser.parse_host_details('<<IP Address>>')
