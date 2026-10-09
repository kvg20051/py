import sys

number_of_errors = 0
number_of_info = 0
number_of_warn = 0

for line in sys.stdin:
    if "ERROR" in line:
        number_of_errors += 1
            if number_of_errors == 1:
            print(line)
    elif "WARN" in line:
        number_of_warn += 1
    elif "INFO" in line:
        number_of_info += 1

print("ERROR", number_of_errors)
print("WARN", number_of_warn)
print("INFO", number_of_info)
