# forensic_robots_txt.py

"""
Description:
    Reads robots.txt of a website and prints what's accessible.

Author:
    Nishant Krishna

Created:
    31 July, 2022
"""

import requests


class ForensicRobotTxt:
    def parse_robots_txt(self, url):
        robots_txt = requests.get(url + '/robots.txt')
        robots_txt_lines = robots_txt.text.split('\n')

        for line in robots_txt_lines:
            if 'Allow' in line:
                print(line)


if __name__ == "__main__":
    robots_txt_parser = ForensicRobotTxt()
    robots_txt_parser.parse_robots_txt('https://www.google.com')
