#!/usr/bin/python3
""" Python Network 01 """

import requests
from sys import argv


def main():
    """
    Send a POST request to the URL with email parameter
    and print the response body
    """

    url = argv[1]
    req = requests.get(url)
    # req = req.text
    if req.status_code == 200:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")


if __name__ == '__main__':
    main()
