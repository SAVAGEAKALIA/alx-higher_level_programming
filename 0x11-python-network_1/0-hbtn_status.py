#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import urlopen


def main():
    """
    Write a Python script that
    fetches alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as e:
        req = e.read()

    print("Body response:")
    print(f"\t- type: {type(req)}")
    print(f"\t- content: {req}")
    req = req.decode('utf-8')
    print(f"\t- utf8 content: {req}")


if __name__ == '__main__':
    main()
