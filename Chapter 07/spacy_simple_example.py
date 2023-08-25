# spacy_simple_example.py

"""
Description:
    A simple example to work with spaCy.

Author:
    Nishant Krishna

Created:
    15 September, 2022
"""

import spacy


class SpacySimpleExample:
    def spacy_process(self):
        # Pretty print spacy info in the markdown format
        print('\n', spacy.info('en_core_web_sm', markdown=True), '\n\n')

        # Load the en_core_web_sm trained pipeline and create a document
        nlp = spacy.load('en_core_web_sm')
        doc = nlp("Earn 60000 rupees every month, Just submit these documents.")

        # Tokenize the document and print all the tokens
        for token in doc:
            print(token.text, token.tag_, spacy.explain(token.tag_))


if __name__ == "__main__":
    spacy_example = SpacySimpleExample()
    spacy_example.spacy_process()
