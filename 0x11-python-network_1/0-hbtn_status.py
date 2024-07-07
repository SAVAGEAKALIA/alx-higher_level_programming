#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import urlopen
from urllib.parse import unquote


def main():
    """
    Write a Python script that
    fetches https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as e:
        req = e.read()

    print(f"Body response:")
    print(f"\t- type: {type(req)}")
    print(f"\t- content: {req}")
    req = unquote(req)
    print(f"\t- utf8 content: {req}")


if __name__ == '__main__':
    main()
