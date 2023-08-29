# crtsh_cert_info.py

"""
Description:
    User crt.sh Python API to get certificate information about a domain.

Author:
    Nishant Krishna

Created:
    16 May, 2022
"""

from pycrtsh import Crtsh
import json


class CrtshCrtInfo:
    def cert_query(self, host):
        """
        Perform a crt.sh certificates lookup for the host

        Args:
            host (string): Host
        """
        crtsh = Crtsh()
        certs = crtsh.search(host)

        # To overcome serialization error for datetime types of object, we can use "default=str" while dumping
        print(json.dumps(certs, indent=4, default=str))


if __name__ == "__main__":
    cert_info = CrtshCrtInfo()
    cert_info.cert_query('<<Host>>')
