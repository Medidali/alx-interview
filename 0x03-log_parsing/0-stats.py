#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items(), key=lambda x: int(x[0])):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) >= 9 and data[-2] in codes:
                try:
                    filesize += int(data[-1])
                    stats[data[-2]] += 1
                except ValueError:
                    pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
