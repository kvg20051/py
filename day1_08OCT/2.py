import sys
numofwarn=0
numoferrors=0
numofinfo=0

for line in sys.stdin:
    date, time, level, msg = line.split(maxsplit=3)
    if level == "WARN":
        print(date, time)
        numofwarn +=1
    elif level == "ERROR":
        print(date, time)
        numoferrors +=1
    elif level == "INFO":
        print(date, time)
        numofinfo +=1

print( "ворнингов:", numofwarn , "ошибок:", numoferrors, "инфо:", numofinfo)


