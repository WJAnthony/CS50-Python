import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.subn(r"\bum\b", "", s.lower()):
        return(int(matches[1]))
    else:
        return(int(0))

if __name__ == "__main__":
    main()
