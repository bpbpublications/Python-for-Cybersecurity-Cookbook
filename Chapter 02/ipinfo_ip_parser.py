# ipinfo_ip_parser.py

"""
Description:
    Use IPInfo to get all the public information about an IP address and then parse few attributes from it.

Author:
    Nishant Krishna

Created:
    16 May, 2022
"""

import json
import ipinfo

ipinfo_accesstoken = '<<Access Token>>'
handler = ipinfo.getHandler(ipinfo_accesstoken)


class IpinfoDetails:

    def get_host_details(self, ip_address):
        try:
            global handler
            ipinfo_details = handler.getDetails(ip_address)
        except:
            ipinfo_details = {}

        # First convert the response to JSON using json.dumps and then load it in a JSON object
        json_data = json.loads(json.dumps(ipinfo_details.all, indent=4))

        # Now print the attributes we need. The get() function can be used to get specific attributes
        print('city: ',json_data['city'])
        print('country: ',json_data['country'])
        print('timezone: ',json_data['timezone'])



if __name__ == "__main__":
    ipinfo_details = IpinfoDetails()
    ipinfo_details.get_host_details('<<IP Address>>')
