#!/usr/bin/python3
""" Python Network 01 """

import requests
from sys import argv


def main():
    """
    Send a request to the URL and
    print the response body or error code
    """

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    dict_letter = {'q': q}

    response = requests.post(url, data=dict_letter)
    # response = response.json()

    content_type = response.headers.get('Content-Type', '')
    if 'application/json' in content_type:
        try:
            json_response = response.json()
            if json_response:
                print(f"[{json_response.get('id')}] {json_response.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
