price = 50
amount_due = 50
amount_given = 0

while True:
    while True:
        print(f"Amount Due: {amount_due}")
        coins = int(input("Insert Coin: "))
        if coins == 25 or coins == 10 or coins == 5:
            break

    amount_given = amount_given + coins
    amount_due = amount_due - coins
    if amount_given >= price:
        break

change = int(amount_given - price)
print(f"Change Owed: {change}")
