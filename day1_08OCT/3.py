import sys
for line in sys.stdin:
    parts = line.split(maxsplit=3)
    if len(parts) < 3:
        continue
    date = parts[0]
    level = parts[2]
