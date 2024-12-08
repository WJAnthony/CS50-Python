def main():
    ## Get user to input a greeting
    greeting = input("Greeting: ")

    ## Determine amount based on greeting
    amount_to_give = value(greeting)

    ## Print greeting
    print("$", amount_to_give, sep="")

def value(greeting):
    if (greeting.lower()).strip().startswith("hello") == True:
        return(int(0))
    elif (greeting.lower()).strip().startswith("h") == True:
        return(int(20))
    else:
        return(int(100))

if __name__ == "__main__":
    main()
