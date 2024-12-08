import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        ## Declare a list
        students = []

        ## Open a CSV file
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            ## Writing to the list
            for row in reader:
                last_name, first_name = row["name"].split(', ')
                students.append({"first_name": first_name, "last_name": last_name, "house": row["house"]})

        ## Opening another CSV file
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])

            ## Writer header to format the new CSV file
            writer.writeheader()

            ## Writing to new CSV file
            for row in students:
                writer.writerow({"first":row["first_name"], "last":row["last_name"], "house":row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
