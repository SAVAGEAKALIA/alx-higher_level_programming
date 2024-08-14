#!/usr/bin/python3
""" Python Network 01 """

import requests


def main():
    """
    Write a Python script that
    Checks for error codes
    Use print statement to output answer
    """

    req = requests.get('https://alx-intranet.hbtn.io/status')
    # req = req.text

    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")


if __name__ == '__main__':
    main()
