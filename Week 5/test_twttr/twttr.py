def main():
    user_input = input("Input: ")
    twtt = shorten(user_input)
    print("Output:", twtt)

def shorten(word):
    ## Copy word into another str
    formatted = word
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    for char in word:
        ## If the char is present in list of vowels
        if char in vowels:
            ## In the copied string, replace the char with nothing
            formatted = formatted.replace(char, "")

    return(formatted)

if __name__ == "__main__":
    main()


