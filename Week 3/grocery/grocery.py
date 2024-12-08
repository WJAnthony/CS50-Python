grocery = {}

while True:
    try:
        item = input("")

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        sorted_grocery = sorted(grocery)
        for item in sorted_grocery:
            print(grocery[item], end=" ")
            print(f"{item.upper()}")
        break
