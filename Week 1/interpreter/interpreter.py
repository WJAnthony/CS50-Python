expression = input("Expression: ")

x, y, z = expression.split(" ")

if (y == "+"):
    answer = round(float(int(x) + int(z)), 1)
elif (y == "-"):
    answer = round(float(int(x) - int(z)), 1)
elif (y == "*"):
    answer = round(float(int(x) * int(z)), 1)
elif (y == "/"):
    answer = round(float(int(x) / int(z)), 1)

print(answer)

