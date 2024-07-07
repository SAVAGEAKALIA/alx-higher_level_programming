#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import urlopen
from sys import argv

arg1 = argv[1]


def main():
    """
    Write a Python script that
    fetches https://alx-intranet.hbtn.io/status
    """

    with urlopen(arg1) as e:
        headers = e.getheaders()

    for key, value in headers:
        if key == 'X-Request-Id':
            print(value)


if __name__ == '__main__':
    main()
