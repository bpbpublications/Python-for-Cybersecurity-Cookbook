# file_metadata.py

"""
Description:
    Prints the well-known metadata for any file similar to Windows (Right click -> Properties), macOS (Right click -> Get Info), or Linux (Right click -> Properties).


Author:
    Nishant Krishna

Created:
    22 December, 2022
"""

import os

# Set the location of the file to read from the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class FileMetadata:
    def print_metadata(self, some_file):
        filename = os.path.join(__location__, some_file)

        # Get the file's metadata
        metadata = os.stat(filename)

        # Print the metadata fields
        print('\nPrinting Metadat for File name:', some_file)
        print('\tSize:', metadata.st_size, 'bytes')
        print('\tLast modified:', metadata.st_mtime)
        print('\tLast accessed:', metadata.st_atime)
        print('\tCreation time:', metadata.st_ctime)
        print('\tMode:', metadata.st_mode)
        print('\tOwner:', metadata.st_uid)
        print('\tGroup:', metadata.st_gid)


if __name__ == "__main__":
    metadata = FileMetadata()
    metadata.print_metadata('Chapter_10.ai')
