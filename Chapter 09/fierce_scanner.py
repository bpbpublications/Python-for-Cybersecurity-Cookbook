# fierce_scan.py

"""
Description:
    Uses Fierce in Kali Linux to perform a scan of a domain


Author:
    Nishant Krishna

Created:
    29 November, 2022
"""

import io
from fierce import fierce
import dns.name
import dns.resolver


class FierceScan:
    def do_dns_lookup(self):
        """
        Perform a DNS lookup for a domain on 'A' records
        """
        resolver = dns.resolver.Resolver()
        query_domain = dns.name.from_text('<domain>')
        dns_record_type = 'A'

        result = fierce.recursive_query(resolver, query_domain, record_type=dns_record_type)

        print ('\nFound A records:')
        for name in result:
            print(name)

    def do_range_expansion(self):
        """
        Expand the range of a subnet
        """
        ip_range = '192.168.19.240/28'

        print ('\nRange Expansion:')
        print(fierce.range_expander(ip_range))


if __name__ == "__main__":
    fierce_scan = FierceScan()
    fierce_scan.do_dns_lookup()
    fierce_scan.do_range_expansion()
