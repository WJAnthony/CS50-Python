import sys
from validator_collection import validators, checkers, errors

def main():
    try:
        email_address = validators.email(input("What's your email? "))
    except errors.EmptyValueError:
        sys.exit("Please enter an email")
    except errors.InvalidEmailError:
        sys.exit("Invalid email")

    is_email_address = checkers.is_email(email_address)
    if is_email_address == True:
        return("Valid")
    else:
        return("Invalid")

if __name__ == "__main__":
    main()


import sys
from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email? ")))

def validate(email):
    email_address = validators.email('test@domain.dev')

    is_email_address = checkers.is_email(email)

    if is_email_address == True:
        return("Valid")
    else:
        return("Invalid")

if __name__ == "__main__":
    main()
