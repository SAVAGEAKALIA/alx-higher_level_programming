#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import urlopen, Request
from sys import argv

arg1 = argv[1]


def main():
    """
    Write a Python script that
    fetches https://alx-intranet.hbtn.io/status
    """

    req = Request(arg1)

    with urlopen(req) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == '__main__':
    main()
