from datetime import date

todays_date = date.today()
print(todays_date)

date_of_birth = date(1999, 1, 1)
print(date_of_birth)

import datetime
import sys
import inflect
import re

class Users:
    def __init__(self, year, month, day):
        date_of_birth = datetime.date(year, month, day)
        return(date_of_birth)

    def __sub__(self, other):
        year = int(self.year - other.year)
        month = int(self.month - other.month)
        day = int(self.day - other.day)
        return timedelta(year, month, day)

    ## Getting today's date
    @classmethod
    def todays_date(cls):
        todays_date = datetime.date.today()
        return(todays_date)

    ## Getting user DOB
    @classmethod
    def get(cls):
        dob = input("Date of Birth: ")
        if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", dob):
            year = int(matches.group(1))
            month = int(matches.group(2))
            day = int(matches.group(3))
            return(year, month, day)
        else:
            sys.exit("Invalid date")

def main():
    user_dob = Users.get()
    todays_date = Users.todays_date()

    ## Subtract the 2 dates
    time = todays_date - user_dob

    ## Print result
    print(time)


if __name__ == "__main__":
    main()
