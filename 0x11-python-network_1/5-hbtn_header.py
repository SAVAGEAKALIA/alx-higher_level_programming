#!/usr/bin/python3
""" Python Network 01 """

import requests
from sys import argv


def main():
    """
    Send a request to the URL and
    print the X-Request-Id header value
    """

    url = argv[1]
    req = requests.get(url)
    # req = req.text
    header = req.headers.get('X-Request-Id')
    print(header)


if __name__ == '__main__':
    main()
