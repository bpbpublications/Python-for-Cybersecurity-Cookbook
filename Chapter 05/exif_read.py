# exif_read.py

"""
Description:
    Read and print Exif (Exchangeable image file format) data of images.

Author:
    Nishant Krishna

Created:
    02 August, 2022
"""

import os
from exif import Image

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class ExifReader:
    def print_image_exif(self, image_file_name):
        """Read the Exif data of the file using 'exif' module

        Args:
            image_file (string): Image file name
        """
        image_file_name = os.path.join(__location__, image_file_name)
        with open(image_file_name, 'rb') as image_file:
            exif_image = Image(image_file)

        # Print all the attribute
        for attribute in exif_image.list_all():
            print(attribute, ': ', exif_image.get(attribute))


if __name__ == "__main__":
    exif_reader = ExifReader()
    exif_reader.print_image_exif('DSCN0010.jpeg')
