#!/usr/bin/python3
""" Python Network 01 """

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


def main():
    """
    Write a Python script that
    Checks for error codes
    Use print statement to output answer
    """
    url = argv[1]

    try:
        # data_req = Request(url, method='POST')

        with urlopen(url) as response:
            html = response.read()

        html = html.decode('utf-8')
        print(f'{html}')
    except HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == '__main__':
    main()
