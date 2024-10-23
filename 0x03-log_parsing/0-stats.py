#!/usr/bin/python3
"""
A script that reads stdin line by line, computes metrics, and outputs
statistics every 10 lines or on keyboard interruption.
"""

import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0
line_count = 0


def print_stats():
    """
    Prints the total file size and counts of status codes
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.split()

            file_size = int(parts[-1])

            status_code = parts[-2]

            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

        except (IndexError, ValueError):
            continue

        # Print the stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:

    print_stats()
    raise

print_stats()
