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

    response = requests.get(f"https://api.github.com/repos/{owner_name}/{rep_name}/commits",
                            headers=headers)

    commits = response.json()
    # print(response)
    for commit in commits:
        # author = commit['commit']['author']['name']
        print(f'{commit["sha"]}: {commit["commit"]["author"]["name"]}')
    # print(f"{response('sha')}: {response('author')}")
    # else:
    # print(response.status_code)


if __name__ == '__main__':
    main()
