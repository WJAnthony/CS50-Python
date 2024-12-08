user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if user_input.strip() == "42":
    print("Yes")
elif (user_input.lower()).strip() == "forty-two":
    print("Yes")
elif (user_input.lower()).strip() == "forty two":
    print("Yes")
else:
    print("No")

