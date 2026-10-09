import sys
count = 0

for line in sys.stdin:
#   line=line.rstrip("\n")
    if "ERROR" in line:
       count +=1

print (count)

