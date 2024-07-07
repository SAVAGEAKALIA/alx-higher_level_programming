#!/usr/bin/python3
"""
Python Network 01
This script fetches the X-Request-Id
header from a URL provided as a command-line argument.
"""

import urllib.request
from sys import argv


def main():
    """
    Main function to execute the script.
    """
    url = argv[1]

    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    urllib.request.install_opener(opener)

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == '__main__':
    main()
