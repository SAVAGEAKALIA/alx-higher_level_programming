#!/usr/bin/python3
""" Python Network 01 """

import requests
from sys import argv


def main():
    """
    Send a request to the URL and
    print the response body or error code
    """
    url = argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")


if __name__ == '__main__':
    main()
