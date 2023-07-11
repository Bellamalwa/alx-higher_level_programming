#!/usr/bin/python3
import sys
import collections

def main():
    total_size = 0
    status_code_counts = collections.defaultdict(int)
    for line in sys.stdin:
        line = line.rstrip()
        data = line.split()
        ip_address, date, method, path, status_code, file_size = data
        total_size += file_size
        status_code_counts[status_code] += 1

        if len(status_code_counts) % 10 == 0 or line == "":
            print("File size: {}".format(total_size))
            for status_code, count in status_code_counts.items():
                print("{}: {}".format(status_code, count))

if __name__ == "__main__":
    main()
