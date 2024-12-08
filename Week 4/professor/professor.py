import random
import sys


def main():
    level = int(get_level())

    score = 0
    for i in range(10):
        attempts = 0
        while True:
            x = generate_integer(level)
            y = generate_integer(level)

            while attempts < 3:
                user_answer = input(f"{x} + {y} = ")
                if int(user_answer) != (int(x) + int(y)) or user_answer.isdigit == False:
                    attempts += 1
                    print("EEE")
                elif int(user_answer) == (int(x) + int(y)):
                    attempts = 0
                    score += 1
                    break
            break

        if attempts == 3:
            print(f"{int(x)} + {int(y)} =", (int(x) + int(y)))

    print(f"Score: {score}")


def get_level():
    while True:
        user_input = input("Level: ")
        if user_input == "1" or user_input == "2" or user_input == "3":
            return (user_input)
        else:
            pass


def generate_integer(level):
    if level == 1:
        return (random.randint(0, 9))
    elif level == 2:
        return (random.randint(10, 99))
    elif level == 3:
        return (random.randint(100, 999))


if __name__ == "__main__":
    main()
