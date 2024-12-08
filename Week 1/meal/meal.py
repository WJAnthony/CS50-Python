def main():
    time = input("What time is it? ")
    number_of_hours = convert(time)

    if (7 <= number_of_hours <= 8):
        print("Breakfast time")
    if (12 <= number_of_hours <= 13):
        print("Lunch time")
    if (18 <= number_of_hours <= 19):
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")

    x = float(int(minutes) / 60)
    return(int(hours) + x)

if __name__ == "__main__":
    main()
