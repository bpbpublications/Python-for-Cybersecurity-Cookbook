# fingerprinting.py

"""
Description:
    A simple way to create fingerprint for a file.

Author:
    Nishant Krishna

Created:
    03 August, 2022
"""

import os
import hashlib

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class Fingerprinting:
    def get_fingerprint(self, filename):

        file_name = os.path.join(__location__, filename)
        with open (file_name, 'r') as file:
            plain_text = file.read()

        # For general encoding, a salt may not be needed
        hashed_text = hashlib.sha256(plain_text.encode()).hexdigest()
        print (hashed_text)


if __name__ == "__main__":
    fingerprinting = Fingerprinting()
    fingerprinting.get_fingerprint('fingerprinting.txt')
