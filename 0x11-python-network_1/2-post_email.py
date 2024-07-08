#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


def main():
    """
    Write a Python script that
    Sends a Post Request
    Use print statement to output answer
    """
    url = argv[1]
    email = argv[2]

    dict_email = {'email': email}
    req = urlencode(dict_email)
    req = req.encode('ascii')

    data_req = Request(url, data=req, method='POST')

    with urlopen(data_req) as response:
        html = response.read()

    html = html.decode('utf8')
    print(f'Your email is: {html}')


if __name__ == '__main__':
    main()
