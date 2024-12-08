def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    # No periods, spaces, or punctuations and length of number plate
    if s.isalnum() and (2 <= length <= 6):

        # if all chars are alphabets
        if s.isalpha():
            return True
        else:
            # first 2 chars are alphabets and last char is a digit
            if s[0:2].isalpha() and s[length -1].isdigit():
                for i in range(length - 1):
                    if s[i].isdigit():
                        # if numbers begin with 0 or alphabet is after the first digit
                        if (s[i] == "0") or s[i + 1].isalpha():
                            return False
                        else:
                            for i in range(length - 1):
                                if s[i].isdigit():
                                    # if alphabet is after a digit
                                    if s[i + 1].isalpha():
                                            return False
                # if pass all requirements, return true
                return True
            else:
                return False
    else:
        return False

main()
