from validator_collection import validators, checkers, errors

def main():
    try:
        validators.email(input("What's your email? "))
        print("Valid")
    except errors.EmptyValueError:
        print("Please enter an email")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()
