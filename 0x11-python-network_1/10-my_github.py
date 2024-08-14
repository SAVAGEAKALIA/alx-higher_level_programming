#!/usr/bin/python3
""" Python Network 01 """

import requests
from requests.auth import HTTPBasicAuth
from sys import argv
import os


def main():
    """
    Send a request to the URL and
    print the X-Request-Id header value
    """

    username = argv[1]
    password = argv[2]
    git_api = "application/vnd.github+json"
    # authorization = os.getenv("GITHUB_TOKEN")
    headers = {'accept': git_api}
    # headers = {
    #     'accept': git_api,
    #     'Authorization': f'Bearer {authorization}',
    #     'User-Agent': 'akaliasaviour@gmail.com',
    #     'X-GitHub-Api-Version': '2022-11-28'}
    basic = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user',
                            headers=headers,
                            auth=basic)
    # response = requests.get('https://api.github.com/user',
    #                         headers=headers)
    # if response.status_code == 200:
    response = response.json()
    # print(response)
    print(response.get('id'))
    # else:
    # print(response.status_code)


if __name__ == '__main__':
    main()
