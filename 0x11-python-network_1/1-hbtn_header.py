#!/usr/bin/python3
"""
Python Network 01
This script fetches the X-Request-Id
header from a URL provided as a command-line argument.
"""

import urllib.request
import urllib.error
from sys import argv


def main():
    """
    Main function to execute the script.
    """
    url = argv[1]
    try:
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
        urllib.request.install_opener(opener)

        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the header")

    except urllib.error.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")


if __name__ == '__main__':
    main()
