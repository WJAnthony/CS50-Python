user_input = input("Input: ")

print("Output: ", end="")
for character in user_input:
    if (character.lower() == "a" or character.lower() == "e"  or character.lower() == "i"  or character.lower() == "o"  or character.lower() == "u"):
        print("", end="")
    else:
        print(character, end="")
print()
