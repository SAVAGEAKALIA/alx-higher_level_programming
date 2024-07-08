#!/usr/bin/env python
""" Python Network 01 """

import requests
from sys import argv


def main():
    """
    Send a request to the URL and
    print the X-Request-Id header value
    """

    rep_name = argv[1]
    owner_name = argv[2]
    git_api = "application/vnd.github+json"
    headers = {'accept': git_api}

    response = requests.get(f"https://api.github.com/repos/"
                            f"{owner_name}/{rep_name}/commits",
                            headers=headers)

    commits = response.json()

    for commit in commits[:10]:
        # author = commit['commit']['author']['name']
        print(f'{commit["sha"]}: {commit["commit"]["author"]["name"]}')


if __name__ == '__main__':
    main()
