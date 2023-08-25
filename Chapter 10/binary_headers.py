# binary_headers.py

"""
Description:
    This program prints binary headers of .jpeg and .ai files


Author:
    Nishant Krishna

Created:
    20 December, 2022
"""

import os
from PyPDF2 import PdfFileReader

# Set the location of the file to read from the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class PrintBinaryHeaders:
    def print_binary_header_jpeg(self, jpeg_file):
        image_file_name = os.path.join(__location__, jpeg_file)
        with open(image_file_name, 'rb') as image_file:
            binary_data = image_file.read(500)
            print(binary_data)

    def print_binary_header_ai(self, ai_file):
        ai_file_name = os.path.join(__location__, ai_file)
        with open(ai_file_name, 'rb') as ai_file:
            ai_file = PdfFileReader(ai_file_name)
            document_info = ai_file.getDocumentInfo()
            print('\n', document_info)


if __name__ == "__main__":
    header = PrintBinaryHeaders()
    header.print_binary_header_jpeg('DSCN0010.jpeg')
    header.print_binary_header_ai('Chapter_10.ai')
