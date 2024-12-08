from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        for font in figlet.getFonts():
            if font == sys.argv[2]:
                user_input = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(user_input))
                sys.exit()
        sys.exit("Include a recognised font")
    else:
        sys.exit("The first command-line argument should be -f or --font")

elif len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    user_input = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user_input))

else:
    sys.exit("Invalid usage")
