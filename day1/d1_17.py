#!/usr/bin/env python3

import sys

def main():
    count = 0
    pattern = input()

    with open('day1/data/app.log', encoding='utf-8') as f:
        for line in f:
            if pattern in line: 
                print(line)
                count +=1
    print(f"число строк где нашли {pattern} равно {count}")

if __name__=="__main__":
    main()
