def main():
    user_input = input("what is your input? ")
    converted = convert(user_input)
    print(converted)

def convert(input):
    converted = (input.replace(":)", "🙂")).replace(":(", "🙁")
    return(converted)

main()
