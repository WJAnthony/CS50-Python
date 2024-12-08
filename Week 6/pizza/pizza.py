import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        ## Declare a list
        pizzas = []

        ## Open the file, append it to the list
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for column1, column2, column3 in reader:
                pizzas.append({"column1":column1, "column2":column2, "column3":column3})

        ## Print the table
        print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
