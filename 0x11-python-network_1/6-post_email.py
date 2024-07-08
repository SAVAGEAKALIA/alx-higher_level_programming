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
    email = argv[2]
    dict_email = {'email': email}
    req = requests.post(url, data=dict_email)
    req = req.text

    print(req)


if __name__ == '__main__':
    main()
