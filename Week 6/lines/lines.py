import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
else:
    ## Open file
    lines = 0
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                ## If line is a comment
                if (line.lstrip()).startswith("#"):
                    lines = lines
                ## If line is just whitespace
                elif line.isspace():
                    lines = lines
                else:
                    lines += 1

        ## Print number of lines of code
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")
