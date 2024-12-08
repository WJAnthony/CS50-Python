import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
        if time := re.search(r"^(\d+)?:?(\d+)? (AM|PM) to (\d+)?:?(\d+)? (AM|PM)$", s):

            ## Set the variables
            start_hour = int(time.group(1))
            start_period = time.group(3)
            end_hour = int(time.group(4))

            ## If single digit
            if time.group(2) == None:
                start_min = int(0)
            else:
                start_min = int(time.group(2))

            if time.group(5) == None:
                end_min = int(0)
            else:
                end_min = int(time.group(5))

            ## Catching invalid inputs
            if start_hour < 0 or end_hour < 0:
                raise ValueError
            elif start_hour > 12 or end_hour > 12:
                raise ValueError
            elif start_min < 0 or end_min < 0:
                raise ValueError
            elif start_min > 59 or end_min > 59:
                raise ValueError
            else:
                ## If start and/or end hours are 12
                if start_hour == 12:
                    start_hour = int(0)
                if end_hour == 12:
                    end_hour = int(0)

                ## If work starts in AM
                if start_period == "AM":
                    return(f"{start_hour:02}:{start_min:02} to {(end_hour + 12):02}:{end_min:02}")
                ## If work starts in PM
                else:
                    return(f"{(start_hour + 12):02}:{start_min:02} to {(end_hour):02}:{end_min:02}")

        ## If not in correct format
        else:
            raise ValueError

if __name__ == "__main__":
    main()
