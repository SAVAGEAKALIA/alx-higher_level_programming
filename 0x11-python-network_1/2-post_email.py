#!/usr/bin/env python
""" Python Network 01 """

from urllib.request import Request, urlopen
from urllib.parse import unquote
from sys import argv


def main():
    """
    Write a Python script that
    fetches https://alx-intranet.hbtn.io/status
    """
    url = argv[1]
    email = argv[2]

    req = email.encode('ascii')

    data = Request(url, req)

    with urlopen(data) as response:
        html = response.read()

    html = html.unquote(html).encode('utf8')
    print(f'Your email is: {html}')


if __name__ == '__main__':
    main()
