user_input = input("camelCase: ")

print("snake_case: ", end="")
for character in user_input:
    if character.islower():
        print(character, end="")
    elif character.isupper():
        print("_" + character.lower(), end="")
print()

