import sys
import art
import csv
import os
from tabulate import tabulate

collection = []
collection.append("Meats")
max = 5


def main():
    # Allow user to exit program at any time
    try:
        # Introduction
        print("Welcome to my CS50p Final Project:")
        # Ascii art
        print(art.text2art("KnowYourFood"))

        # Instructions
        print("This program allows you to compare and contrast the nutriential values of up to 5 different food options within a certain food group.")
        print("Purpose: Aid users when selecting the best option from a certain food group for them.")
        print()
        print("To exit the program at any time: press 'CRTL' + 'C'.")
        print()

        menu_display = True
        while menu_display == True:

            # Menu
            menu_table = [[1, "List_of_food_groups"], [2, "Compare"], [3, "Input new food options"]]
            print(tabulate(menu_table, headers=["Option:", "Menu:"], tablefmt="pretty"))
            print()

            # User input
            user_option = input("Enter menu option number (1,2,3): ")

            # 1 - Food lists
            global collection

            # list of lists
            if user_option == "1" or user_option.lower() == "one":
                print()
                print("This is the collection of lists of food options, sorted by alphabetical order:")

                for index, val in enumerate(sorted(collection)):
                    print((index + 1, val))

                while True:
                    try:
                        print()
                        food_group = input("Press enter a food group: ")

                        # Get all items from a food-group list
                        list = get_list(food_group)
                        break
                    except ValueError:
                        print("Invalid input")

                # Printing all available options
                for i in range(len(list)):
                    print(f"{list[i]}, ", end="")
                print()

                # Return to menu
                if to_menu() == True:
                    pass
                else:
                    break

            # 2 - Compare
            if user_option == "2" or user_option.lower() == "two":
                print()
                print(
                    "Here you can compare the nutriental value of up to 5 different food options within a particular food group")

                # Print out collection of list
                print("This is the collection of lists of food options, sorted by alphabetical order:")
                for index, val in enumerate(sorted(collection)):
                    print((index + 1, val))

                # User to enter list of choice
                print()
                chosen_list = input("Enter a food group: ")

                # If Meats list was chosen
                if chosen_list.lower() == "meats":

                    # Create list of data of meats the user has selected
                    meats_data = []

                    # Break from loop when brk is changed to True
                    brk = False
                    while brk == False:

                        # User to input a meat
                        print()
                        while True:
                            user_meat = input("Enter meat of choice: ").strip()
                            if check_meat(user_meat) == True:
                                break
                            else:
                                print("Invalid input, try again.")

                        # Get data on meat
                        meat_data = get_meat(user_meat)

                        # Append the data of the selected meat to meat_data list
                        if meat_data in meats_data:
                            pass
                        else:
                            meats_data.append(meat_data)

                        # Tell user which meats are currently chosen
                        print(f"\nCurrently selected {len(meats_data)}/{max} Meats: ", end="")
                        for i in meats_data:
                            print(f"{i['Name']}, ", end="")

                        # Once the list has data for the maximum allowed
                        if len(meats_data) == max:
                            break

                        # Add more meats
                        while True:
                            user_choice = (
                                input("\nDo you wish to add more meats? (Y or N): ")).strip().lower()
                            if user_choice == "y" or user_choice == "yes":
                                print()
                                break
                            elif user_choice == "n" or user_choice == "no":
                                brk = True
                                break
                            else:
                                pass

                    # Print out all selected meats
                    print(f"\nYou have selected the following as your final list for analysis:")
                    for i in meats_data:
                        print(f"{i['Name']}, ", end="")

                    # User confirmation
                    input("\nPress enter to continue: ")

                    # Print table for comaprison
                    print()
                    header = meats_data[0].keys()
                    rows = [x.values() for x in meats_data]
                    print(tabulate(rows, header, tablefmt='grid'))
                    print()

                # Return to menu
                if to_menu() == True:
                    pass
                else:
                    break

            # 3 - Input new food options or create new list
            if user_option == "3" or user_option.lower() == "three":

                # List of list
                print()
                print("This is the collection of lists of food options, sorted by alphabetical order:")

                # list of lists
                for index, val in enumerate(sorted(collection)):
                    print((index + 1, val))
                    print()

                while True:
                    # Add onto existing list or create new list
                    user_input = input(
                        "Option A: add food options to an existing list, Option B: create new list. Option? ")

                    # User wishes to append to existing list
                    if (user_input.lower()).strip() == "a":

                        # User to enter list of choice
                        chosen_list = input("Enter a food group: ")

                        # If Meats list was chosen
                        if chosen_list.lower() == "meats":

                            # Get nutriental information from user
                            name = input("Name of meat: ")
                            calories = int(input("Calories per 100g (kcal): "))
                            protein = int(input("Protein(g) per 100g: "))
                            fat = float(input("Fats(g) per 100g: "))
                            sf = float(input("Saturated Fats(g) per 100g: "))
                            muf = float(input("Monounsaturated Fats(g) per 100g: "))
                            puf = float(input("Polyunsaturated Fats(g) per 100g: "))

                            # Confirmation with user
                            print(f"name: {name}, calories: {calories}g, protein: {
                                  protein}g, fat: {fat}g, SF: {sf}g, MUF: {muf}g, PUF: {puf}g ")
                            input("Press enter to continue")

                            # add to meats list
                            add_to_meats_list(chosen_list, name, calories, protein, fat, sf, muf, puf)
                            print("Successfully added!")
                            break

                        else:
                            print("Invalid input")
                            pass

                    # User wishes to create a new list
                    elif (user_input.lower()).strip() == "b":
                        # Ask users for name and nutrients measured
                        name = input("What is the name of this food group? ")
                        nutrients = input(
                            "List all nuritents measured, including name, sparated by commas with no spaces: ")
                        field = nutrients.split(',')

                        # write to a new CSV file
                        with open(f"{name}.csv", 'w') as file:
                            writer = csv.writer(file)
                            writer.writerow(field)

                        print("Successfully added!")
                        break

                    # If neither option A or B was selected
                    else:
                        pass

                # Return to menu
                if to_menu() == True:
                    pass
                else:
                    break

            # Invalid input
            else:
                print("Please try again")

    except KeyboardInterrupt:
        # Clearing data
        os.system("clear")

        # Thank you message
        print("Thank you for visiting my CS50 python final project: KnowYourFood. \nCopyright: Anthony Chow 2024\n")
        sys.exit("You have successfully closed this programme, goodbye!")


def get_list(food_group):
    global collection
    options_list = []
    if food_group.capitalize() in collection:
        with open(f"{food_group.lower()}.txt", "r") as file:
            for line in sorted(file, key=lambda line: line[0]):
                options_list.append(line.strip())
    else:
        raise ValueError

    return options_list


# For user to return to menu or quit
def to_menu():
    while True:
        user_answer = input("Next action? (Menu or Exit): ")
        if user_answer.lower() == "menu":
            return True
        elif user_answer.lower() == "exit":
            return False

# Add food options to meats list
def add_to_meats_list(chosen_list, name, calories, protein, fat, sf, muf, puf):
    with open(f"{chosen_list.lower()}.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "calories", "proteins", "fat",
                                "saturated_fats(SF)", "monounsaturated_fats(MUF)", "polyunsaturated_fats(PUF)"])
        writer.writerow({"name": name, "calories": calories, "proteins": protein, "fat": fat,
                          "saturated_fats(SF)": sf, "monounsaturated_fats(MUF)": muf, "polyunsaturated_fats(PUF)": puf})

# Check if meat exist in meats list
def check_meat(user_meat):
    while True:
        # Assume user_meat is a string
        is_string = True

        # Prevent user from just pressing enter
        if user_meat.isalpha() == False:
            is_stirng = False

        # Open CSV file
        if is_string:
            with open("meats.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == user_meat.capitalize():
                        return True
                return False

        # If numbers were input or enter was just hit
        else:
            return False

## Get meat's data
def get_meat(user_meat):
    data = {}
    with open("meats.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] == user_meat.capitalize():
                return {"Name": row["name"], "Calories(Kcal)": row["calories"], "Proteins(g)": row["proteins"], "Fat(g)": row["fat"], "Saturated fats(g)": row["saturated_fats(SF)"], "Monounsaturated fats(g)": row["monounsaturated_fats(MUF)"], "Polyunsaturated fats(g)": row["polyunsaturated_fats(PUF)"]}


if __name__ == "__main__":
    main()
