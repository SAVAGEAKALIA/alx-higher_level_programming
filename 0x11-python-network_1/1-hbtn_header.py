#!/usr/bin/python3
"""
Python Network 01
This script fetches the X-Request-Id
header from a URL provided as a command-line argument.
"""

from urllib.request import urlopen, Request
from sys import argv


def main():
    """
    Main function to execute the script.
    """
    arg1 = argv[1]
    req = Request(arg1)

    with urlopen(req) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == '__main__':
    main()
