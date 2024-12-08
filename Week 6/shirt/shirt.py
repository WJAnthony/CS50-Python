import sys
import csv
import os
from PIL import Image, ImageOps

root_ext1 = os.path.splitext(sys.argv[1])
root_ext2 = os.path.splitext(sys.argv[2])

extensions = [".jpg", ".png", ".jpeg"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif root_ext1[1] not in extensions:
    sys.exit("Invalid input")
elif root_ext2[1] not in extensions:
    sys.exit("Invalid input")
elif root_ext1[1] != root_ext2[1]:
    sys.exit("Input and output have different extensions")
else:
    try:
        ## Determine size of shirt
        shirt = Image.open("shirt.png")
        size = shirt.size

        ## Resize background to fit shirt
        background = Image.open(sys.argv[1], mode='r')
        resized = ImageOps.fit(background, size)

        ## Paste shirt onto resized image
        resized.paste(shirt, shirt)

        ## Save image
        final = resized.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
