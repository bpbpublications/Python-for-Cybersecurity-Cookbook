# nslookup_info.py

"""
Description:
    Test "nslooup" operation on an IP Address.

Author:
    Nishant Krishna

Created:
    14 May, 2022
"""

from nslookup import Nslookup


class NsLookup:
    def nslookup(self, domain):
        """
        Perform a DNS lookup for a host.

        Args:
            domain (string): Domain that you want to find IP Address for
        """

        # In the below query, we have used one of the Google's DNS servers
        dns_query = Nslookup(dns_servers=["8.8.8.8"])
        dns_record = dns_query.dns_lookup(domain)
        print(dns_record.response_full, dns_record.answer)


if __name__ == "__main__":
    ns_lookup = NsLookup()
    ns_lookup.nslookup("google.com")
