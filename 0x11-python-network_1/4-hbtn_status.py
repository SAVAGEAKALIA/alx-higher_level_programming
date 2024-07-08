#!/usr/bin/env python
""" Python Network 01 """

import requests


def main():
    """
    Write a Python script that
    Checks for error codes
    Use print statement to output answer
    """

    req = requests.get('https://alx-intranet.hbtn.io/status')
    req = req.text

    print("Body response:")
    print(f"\t- type: {type(req)}")
    print(f"\t- content: {req}")


if __name__ == '__main__':
    main()
