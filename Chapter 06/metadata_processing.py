# metadata_extraction.py

"""
Description:
    Extracts the metadata from a Word file and checks if the file has Confidential or Classified tag or text in the properties.

Author:
    Nishant Krishna

Created:
    22 August, 2022
"""

import os
import zipfile

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class MetadataProcessor:
    def process_metadata(self) -> None:
        # Extract metadata for Word file
        docx_file = os.path.join(__location__, 'metadata_extraction_sample.docx')
        word_document = zipfile.ZipFile(docx_file)

        # document.extractall() will extract the entire Word document into its components including various XML files
        word_extraction_path = os.path.join(__location__, 'metadata_extraction_sample_word')
        word_document.extractall(word_extraction_path)

        # Read the XML file
        xml_file = open(os.path.join(word_extraction_path, 'docProps/core.xml'))
        xml_str = xml_file.read()

        print('\nMetadata for Word file:\n', xml_str)

        if 'Confidential'.lower() in xml_str.lower() or 'classified'.lower() in xml_str.lower():
            print('\nThe document is tagged confidential or classified.')


if __name__ == "__main__":
    metadata_processor = MetadataProcessor()
    metadata_processor.process_metadata()
