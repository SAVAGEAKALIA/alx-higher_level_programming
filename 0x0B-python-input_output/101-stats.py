#!/usr/bin/python3
""" File for the  Input/Output Project"""
import sys


def print_metrics(total_size, status_code_counts):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(code, count))


def process_line(line, total_size, status_code_counts):
    """Processes a line and updates the metrics."""
    try:
        elements = line.split()
        size = int(elements[-1])
        code = elements[-2]
        total_size += size

        # Update status code count
        if code in status_code_counts:
            status_code_counts[code] += 1
        else:
            status_code_counts[code] = 1

    except (ValueError, IndexError):
        pass  # Ignore lines that don't match the expected format

    return total_size, status_code_counts


def main():
    total_size = 0
    status_code_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_code_counts = process_line(line, total_size, status_code_counts)

            # Print metrics every 10 lines
            if i % 10 == 0:
                print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption
        print_metrics(total_size, status_code_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
