#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print Hidden Directories"""

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
