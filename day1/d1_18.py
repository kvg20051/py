#!/usr/bin/env python3

import sys

def main():
    count=0
    pattern = input()
    with open("day1/data/app.log") as f:
        for line in f:
            if pattern in line:
                print(line)

if __name__=="__main__":
    main()
