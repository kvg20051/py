import sys
count=0
words = sys.stdin.read().split()
for word in words:
    count +=1

print(count)
