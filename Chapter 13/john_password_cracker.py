# john_password_cracker.py

"""
Description:
    Demonstrates how to crack password using John The Ripper from Python


Author:
    Nishant Krishna

Created:
    13 June, 2023
"""

import os
import platform

# Set the location of the file to read from the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class JohnPasswordCracker:
    def crack_password(self, passwords):
        password_file = os.path.join(__location__, passwords)
        os.system("john --format=crypt " + password_file)


if __name__ == "__main__":
    john = JohnPasswordCracker()
    john.crack_password("passwords.out")
