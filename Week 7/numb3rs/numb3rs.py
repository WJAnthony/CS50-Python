import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if numbers := re.search(r"^(\d*)\.(\d*)\.(\d*)\.(\d*)$", ip):
        if int(numbers.group(1)) > 255 or int(numbers.group(1)) < 0:
            return False
        elif int(numbers.group(2)) > 255 or int(numbers.group(2)) < 0:
            return False
        elif int(numbers.group(3)) > 255 or int(numbers.group(3)) < 0:
            return False
        elif int(numbers.group(4)) > 255 or int(numbers.group(4)) < 0:
            return False
        else:
            return True

    return False

if __name__ == "__main__":
    main()
