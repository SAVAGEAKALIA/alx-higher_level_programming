#!/usr/bin/python3
""" File for the  Input/Output Project"""

import sys

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
code_counts = {}  # Initialize an empty dictionary to store code counts
total_file_size = 0
line_count = 0

try:
    """Processes a line and updates the metrics."""
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_file_size += file_size
        code_counts[status_code] = code_counts.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()  # Print final statistics on interruption


def print_statistics():
    """Prints the computed metrics."""
    print("File size:", total_file_size)

    print("Number of lines by status code:")
    for code in sorted(code_counts):  # Print codes in ascending order
        print(f"{code}: {code_counts[code]}")
