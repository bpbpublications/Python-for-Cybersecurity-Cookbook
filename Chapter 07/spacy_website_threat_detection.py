# spacy_website_threat_detection.py

"""
Description:
    Detecting potential threat in a website using BeautifulSoup and spaCy.

Author:
    Nishant Krishna

Created:
    01 October, 2022
"""

import spacy
from bs4 import BeautifulSoup
import requests
from collections import Counter


class SpacyThreatDetection:
    def spacy_process(self):

        # Fetch the URL
        test_url = 'https://medium.com/@nishantkrishna/testing-the-limits-of-human-creativity-using-an-online-experiment-on-r-place-on-reddit-84614759af57'
        website = requests.get(test_url)
        website_html = website.content

        # Extract only text from the content
        soup = BeautifulSoup(website_html, 'html.parser')
        input_text = ' '.join(soup.getText().split())
        # print(input_text)

        # Now find out the named entities and their counts. As per spaCy, a named entity is a “real-world object”
        # that’s assigned a name
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(input_text)
        print('\n', doc.ents, '\n')

        # Let's print the labels and their counts
        doc_labels = [ent.label_ for ent in doc.ents]
        print(Counter(doc_labels), '\n')

        # Print most common items in the text
        doc_common_items = [ent.text for ent in doc.ents]
        print(Counter(doc_common_items).most_common(5))


if __name__ == "__main__":
    space_detection = SpacyThreatDetection()
    space_detection.spacy_process()
