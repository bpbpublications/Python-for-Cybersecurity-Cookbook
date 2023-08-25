# metadata_extraction.py

"""
Description:
    Extracts the metadata from PDF, Word and Excel files.

Author:
    Nishant Krishna

Created:
    21 August, 2022
"""

import os
from PyPDF2 import PdfReader
import zipfile
import xml.dom.minidom

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class MetadataExtractor:
    def extract_metadata(self) -> None:
        # Extract metadata for PDF file
        pdf_file = os.path.join(__location__, 'metadata_extraction_sample.pdf')
        pdf_reader = PdfReader(pdf_file)
        print('\nMetadata for PDF file: ', pdf_reader.metadata)
        print('\nCheck if PDF file encrypted: ', pdf_reader.getIsEncrypted())

        # Extract metadata for Word file
        docx_file = os.path.join(__location__, 'metadata_extraction_sample.docx')
        word_document = zipfile.ZipFile(docx_file)

        # document.extractall() will extract the entire Word document into its components including various XML files
        word_extraction_path = os.path.join(__location__, 'metadata_extraction_sample_word')
        word_document.extractall(word_extraction_path)
        xml_dom = xml.dom.minidom.parse(os.path.join(word_extraction_path, 'docProps/core.xml'))
        print('\n\nMetadata for Word file: \n', xml_dom.toprettyxml())

        # Extract metadata for Excel file
        xlsx_file = os.path.join(__location__, 'metadata_extraction_sample.xlsx')
        excel_document = zipfile.ZipFile(xlsx_file)

        # document.extractall() will extract the entire Word document into its components including various XML files
        excel_extraction_path = os.path.join(__location__, 'metadata_extraction_sample_excel')
        excel_document.extractall(excel_extraction_path)
        xml_dom = xml.dom.minidom.parse(os.path.join(excel_extraction_path, 'docProps/core.xml'))
        print('\n\nMetadata for Excel file: \n', xml_dom.toprettyxml())


if __name__ == "__main__":
    extractor = MetadataExtractor()
    extractor.extract_metadata()
