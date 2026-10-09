#!/usr/bin/env python3

import sys

def main():

    num_of_warn=0
    num_of_errors=0
    num_of_info=0
    num_of_lines=0
    first_error_time = None
    last_error_time = None

    for line in sys.stdin:
        num_of_lines +=1
        parts = line.split()
        if len(parts) < 2:
            continue
        if parts[2] == "WARN":
            num_of_warn +=1
        if parts[2] == "INFO":
            num_of_info +=1
        if parts[2] == "ERROR":
            num_of_errors +=1
            last_error_time = parts[1]
            if num_of_errors == 1:
                first_error_time = parts[1]

    print(f"Total number of lines: {num_of_lines}")
    print(f"Total number of WARNINGS: {num_of_warn}")
    print(f"Total number of INFO: {num_of_info}")
    print(f"Total number of ERROR: {num_of_errors}")

    print(f"First ERRORS time: {first_error_time}")
    print(f"Last ERRORS time: {last_error_time}")


if __name__ == "__main__":
   main()
