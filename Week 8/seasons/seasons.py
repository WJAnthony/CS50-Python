from datetime import date
import sys
import re
import inflect


p = inflect.engine()


def main():
    ## Calculate age of user
    dob = user_dob(input("Date of Birth: "))
    age = calculate_age(dob, todays_date())
    print(age)


def user_dob(dob):
        if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", dob):
            year = int(matches.group(1))
            month = int(matches.group(2))
            day = int(matches.group(3))

            ## Ensuring values are valid
            if year < 1 or year > 9999:
                raise ValueError("Invalid year")
            if month < 1 or month > 12:
                raise ValueError("Invalid month")

            ## Returning DOB in datetime format
            return date(year, month, day)

        else:
            sys.exit("Invalid Date")

def todays_date():
    ## Returning today's date in datetime format
    todays_date = date.today()
    return(todays_date)


def calculate_age(user_dob, todays_date):
    ## Determing the difference in time, returned in a timedelta format (days, seconds, microseconds)
    age = todays_date - user_dob

    ## Converting days to mins
    mins = int(age.days) * 1440

    ## Formatting numbers to words + capitalizing
    words = (p.number_to_words(mins, andword="")).capitalize()
    return (f"{words} minutes")


if __name__ == "__main__":
    main()
