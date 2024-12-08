import sys

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            value = gauge(percentage)
            print(value)
            sys.exit()
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(fraction):
    x, y = fraction.split('/')

    if x.isnumeric() == False:
        raise ValueError
    elif y.isnumeric() == False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(y) < int(x):
        raise ValueError
    else:
        percentage = float(int(x)/int(y))
        return (round(percentage * 100))

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
