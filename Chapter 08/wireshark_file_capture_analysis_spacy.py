# wireshark_file_capture_analysis_spacy.py

"""
Description:
    Uses spaCy to perform the analysis of a Wireshark file capture file (PCAP file).


Author:
    Nishant Krishna

Created:
    04 November, 2022
"""

import os
import pyshark
import spacy
from collections import Counter

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class WiresharkFileCaputureAnalysisSpacy:
    def do_capture_analysis(self):
        # Read the PCAP (Packet Capture) file
        pcap_file_name = os.path.join(__location__, 'output.pcap')
        capture = pyshark.FileCapture(pcap_file_name)

        # Get the layer names for each of the packets and append them to the array
        packet_layers = []
        num_packets = 0
        for packet in capture:
            packet_layers.append(packet.layers)
            num_packets += 1

        # Print all the layer names
        print(packet_layers, '\n')

        # Join all the elements into a single string for analysis for spaCy
        packet_layers_str = ' '.join([str(packet) for packet in packet_layers])

        # Load the en_core_web_sm trained pipeline and create a document
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(packet_layers_str)

        # Get all the individual words after filtering out the ones we are not interested in, and then get the word frequency
        words = [token.text for token in doc if 
            not token.is_stop 
            and not token.is_punct 
            and not token.is_left_punct 
            and not token.is_right_punct]
        word_frequency = Counter(words)

        # Perform simple analysis on the layers
        print('Number of packets: ', num_packets)
        print('Word frequency for the packets: ', word_frequency, '\n')

        num_layers = word_frequency['Layer']
        print('Number of total protocol layers: ', num_layers)
        print('Number of average layers per packet: ', num_layers / num_packets, '\n')

        num_layers_tls = word_frequency['TLS']
        print('Number of protocol packets with TLS: ', num_layers_tls, ' out of ', num_packets, '\n')


if __name__ == "__main__":
    wireshark_file_capture_analysis_spacy = WiresharkFileCaputureAnalysisSpacy()
    wireshark_file_capture_analysis_spacy.do_capture_analysis()
