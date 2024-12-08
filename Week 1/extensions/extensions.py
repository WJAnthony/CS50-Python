file = input("File name: ")

if (file.lower()).strip().endswith(".gif") == True:
    print("image/gif")
elif (file.lower()).strip().endswith(".jpg") == True:
    print("image/jpeg")
elif (file.lower()).strip().endswith(".jpeg") == True:
    print("image/jpeg")
elif (file.lower()).strip().endswith(".png") == True:
    print("image/png")
elif (file.lower()).strip().endswith(".pdf") == True:
    print("application/pdf")
elif (file.lower()).strip().endswith(".txt") == True:
    print("text/plain")
elif (file.lower()).strip().endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")


