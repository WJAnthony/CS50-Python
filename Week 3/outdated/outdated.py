months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_input = input("Date: ").strip()
        month, day, year = user_input.split("/")

        if day.isdigit() == False:
            pass
        elif month.isdigit() == False:
            pass
        elif year.isdigit() == False:
            pass
        elif int(day) > 31:
            pass
        elif int(month) > 12:
            pass
        else:
            print(f"{int(year):02}" + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")
            break

    except ValueError:
        month, day, year = user_input.split(" ")

        if month.isalpha() == False:
            pass
        elif "," not in day:
            pass
        elif day.strip(',').isdigit() == False:
            pass
        elif int(day.strip(',')) > 31:
            pass
        else:
            month_rank = int (months.index(month) + 1)

            print(f"{int(year):02}" + "-" + f"{month_rank:02}" + "-" + f"{int(day.strip(',')):02}")
            break

    except ValueError:
        pass
