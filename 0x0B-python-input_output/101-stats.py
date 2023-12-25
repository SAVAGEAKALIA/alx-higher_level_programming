#!/usr/bin/python3
""" File for the  Input/Output Project"""
import sys

# Initialize variables to store metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input lines from stdin
    for line in sys.stdin:
        """Processes a line and updates the metrics."""
        elements = line.split()

        # Check if there are enough elements in the line
        if len(elements) >= 2:
            # Extract status code and file size from the elements
            status_code = int(elements[-2])
            file_size = int(elements[-1])
            total_size += file_size

            # Update the count for the status code
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print("""File size: {}""".format(total_size))
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print("""{}: {}""".format(code, count))

except KeyboardInterrupt:
    pass
finally:
    """ Print final metrics after interruption """
    print("""File size: {}""".format(total_size))
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("""{}: {}""".format(code, count))
