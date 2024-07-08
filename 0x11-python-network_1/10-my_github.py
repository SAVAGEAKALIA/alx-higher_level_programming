#!/usr/bin/env python
""" Python Network 01 """

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main():
    """
    Send a request to the URL and
    print the X-Request-Id header value
    """

    username = argv[1]
    password = argv[2]
    git_api = "application/vnd.github+json"
    headers = {'accept': git_api}
    basic = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user', headers=headers, auth=basic)
    # if response.status_code == 200:
    response = response.json()
    print(response.get('id'))
    # else:
    # print(response.status_code)


if __name__ == '__main__':
    main()
