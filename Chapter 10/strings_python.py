# strings_python.py

"""
Description:
    A rudimentary Python equivalent of Linux 'strings' command which can find all the strings in a given binary file.


Author:
    Nishant Krishna

Created:
    20 December, 2022
"""

import os
import re

# Set the location of the file to read from the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class PythonStrings:
    def print_strings_in_file(self, bin_file):
        bin_file_name = os.path.join(__location__, bin_file)

        with open(bin_file_name, 'rb') as input_file:
            data = input_file.read()
        strings = re.findall(b'[\x20-\x7e]{4,}', data)

        print([str.decode() for str in strings])


if __name__ == "__main__":
    strings = PythonStrings()
    strings.print_strings_in_file('Chapter_10.ai')
