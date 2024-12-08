# Havard CS50 Python Final Project: KnowYourFood

## Introduction
This file explains my final project for the Havard CS50p course on edx. The purpose of this file is to document my project thoroughly as well as all aspects of its functionality. This later part of this section describes what my project is, and the later sections will explain each of the files I have coded for this project.


### Details
Details:
- Project title: KnowYourFood
- Name: Anthony Chow
- Github username: WJAnthony
- EDx username: Anthony_2471
- Country & City: Singapore, Singapore
- Video Demo: <URL https://youtu.be/N2qZLw6V8Ec?si=TBwspVxuLEVFBTlj>


### Inspiration
he inspiration for this project comes from a personal hobby of mine: the Gym.

Due to the numerous health benefits that going to the gym regularly brings, me and my friends have began our fitness journey at the start of the the year. I visit the gym regularly, arround 4 to 5 times a weeks for 2 hours, with a focus on lifting weights.
My goal going to the gym is to increase my lean muscle mass AKA building more muscles.

However, muscle mass is not just build in the gym but also in the kitchen. According to the American College of Sports Medicine: "to increase muscle mass in combination with physical activity, it is recommended that a person that lifts weights regularly should eat a range of 1.2-1.7 grams of protein per kilogram of body weight per day".

Therefore, my final project is created as a platform to allow users to store nutriental information on various food options within various food groups. Users will be able to create new food group list or add new food options into existing food groups. Users will then be able to compare the nutriential values of up to 5 different options within a particular food group.

To get users started, I have already included a meats food-group list as well as nutritional information on 30 of the most common meat options, in a separate CSV file. Users will then be able to compare up to 5 meat options based on 5 nutritional values (Calories, Protein, Fat, Saturated fats, Monounsaturated fats and Polyunsaturated fats) to determine which meat is most suitable for the health requirements.

This program is built for users who have at least a basic understanding of python as it is meant to be adaptable, allowing it to grow and expand to the needs of the users. While currently there is only one food-group list, meats, users are able to add more. As such the add_to_meats_list, get_meats and check_meat functions are written similar to templates. For other food groups, users are able to duplicate these functions for the new food-group, just changing the relevant names as well as the nutritional values compared within that particular food group. Users can then utilise code written under "if meats list was selected" for new food-group.


## Description
My final project is created as a platform to allow users to store nutriental information on various food options within various food groups. Users will be able to create new food group list or add new food options into existing food groups. Users will then be able to compare the nutriential values of up to 5 different options within a particular food group.

To get users started, I have already included a meats food-group list as well as nutritional information on 30 of the most common meat options, in a separate CSV file. Users will then be able to compare up to 5 meat options based on 5 nutritional values (Calories, Protein, Fat, Saturated fats, Monounsaturated fats and Polyunsaturated fats) to determine which meat is most suitable for the health requirements.

This version of the program is built for users who have at least a basic understanding of python as it is meant to be adaptable, allowing it to grow and expand to the needs of the users. While currently there is only one food-group list, meats, users are able to add more. As such the add_to_meats_list, get_meats and check_meat functions are written similar to templates. For other food groups, users are able to duplicate these functions for the new food-group, just changing the relevant names as well as the nutritional values compared within that particular food group. Users can then utilise code written under "if meats list was selected" for new food-group.

lastly, this version of this program is only version 1. I will continue to improve the program through various versions to add more features and functionality as well as removing the need to reuse code whenever there is a new food-group implemented. This way new food-groups can not only be added seamlessly but displayed seamlessly as well, allowing users with no programming knowledge to use it.

To use this program, the following is required:
1. 'project.py' file
2. pip installable modules (in requirements.txt)
    - sys
    - art
    - csv
    - os
    - tabulate


## Content
### Main file: "project.py"
Contains the main body of the code as well as 5 other functions:
- main
- get_list
- to_menu
- add_to_meats_list
- check_meat
- get_meat


#### main
This is the main function for projects.py. It first displays a welcome message for users upon first entering the program. There will be an explanation of what the program is as well as its purpose. Subsequently, a menu table will be displayed with 3 menu options for users to choose from via an input prompting them to input their menu option. Should the user input an invalid menu option, they will be prompted to re-enter a menu option.

Additionally, if the user wishes to end the program, they can simply press "crtl" and "c". This will automatically clear the users terminal and a summary message will be printed, thanking users for using the program.

The main section of the main function is split into 3 sections, each one containing the code for each of the 3 menu options that users can access.

First, if the user types "1" or "one", a list of available food-group lists will be displayed as well as a prompt below for users to enter the name of the list so that they can view all food options within that particular food group list. If the user enters a food-group that is not currently available, user will be re-prompted until they input a valid food-group. The get_list function is then called and returns a list of all the food options within that particular food group which will then be printed out for users.

Second, if the user types "2" or "two", a list of available food-group lists will be displayed as well as a prompt below for users to enter the name of the list so that they can compare up to 5 unique food options within that particular food group list. If the user enters a food-group that is not currently available, user will be re-prompted until they input a valid food-group.

Since there is only a meats list, users are curently able to enter meats only. Following which, a list called meats_data is created to store the data of the selected meat options. The user will then be prompted for a meat option that they would like to compare, the check_meat function will then be called in order to confirm that option is inside the meats.csv file, if not, users will be re-prompted until they input a valid input. If the meat option is inside, the get_meat_data will be called to get the data on the selected meat option which will then be appended to the meats_data list. A message will then be printed informing them how many and what meat options they have chosen to compare and whether they wish to add more option provided less than the max number of options have been chosen. Following which, a confirmation message will be printed for user verification. Upon pressing "enter", the tabulate function from the tabulate module will then be called to print out all the nutritional values of all the chosen meat options in a an easy-to-read table allowing users to easy compare between the various options.

Third, if the user types "3" or "three", a list of available food-group lists will be displayed. Next there will be 2 options for users to choose from, option A will be adding additional food options to existing food-group list and option B will be creating new food-group list. Below will then be a prompt for users to input their desired option, users will also be re-prompted until they enter a valid option.

If users enter A, they will then be further prompted to choose which food-group list they would like to add food options to. Since there is currently only a meats list, when the user chooses it, they will then be prompted to provide the name of the meat they wish to add as well as its nutritional values including its calories, protein, fat, saturated fats, monounsaturated fats and polyunsaturated fats. Next, a confirmation message is printed for users to verify all necessary information, upon pressing "enter", the add_to_meats_list function will be called and the new meat option will be added to the meats.csv file. If successful, a success message will be printed.

If users enter B, they will be prompted for the name of the new food-group list they wish to create. Next, they will be prompted to enter the nutriental values that will be used as the measuring factors within that food group, in a single line with commas but no spacing. Following that, a CSV with the name of that food-group will be created with name + the measurable nutrients as fieldheaders within that file. If successful, a success message will be printed.

Lastly, at the end of each of the 3 menu options, the to_menu function will be called, allowing users to either return to the main menu or exit the program entirely.


#### get_list
The get_list function takes name of a food-group as an argument. An empty list called options_lists is also created. If the food group does not exit in the global collection of food-group list, the function will raise a ValueError. Otherwise, if food group entered is valid, the .txt file of that particular food group will be opened as file and sorted using an annoymous function, and for every row in the file, the name of the options is added to the options_list list. This list will then be returned after all options have been appended to it.


#### to_menu
Users will be prompted for their next action, to go back to the menu or exit the program entirely. If they choose menu, the function will return True but if they choose Exit, function will return False. If neither options are selected, users will be re-prompted until they input a valid option. If function returns True, the menu table will be displayed again while if function returns exit, the program will exit.


#### add_to_meats_list
This function is called when user wishes to add additional meat option into the meats.csv file. This function takes in multiple arguments as shown: def add_to_meats_list(chosen_list, name, calories, protein, fat, sf, muf, puf):. The function then opens the correct csv file, using the chosen_list, using the csv.DictWriter with "name, calories, protein, fat, sf, muf, puf" as fieldnames. Next the writerow writes this into the csv file: writerow({"name": name, "calories": calories, "proteins": protein, "fat": fat,"saturated_fats(SF)": sf, "monounsaturated_fats(MUF)": muf, "polyunsaturated_fats(PUF)": puf}). The function does not return anything when executed successfully.


#### check_meat
This function also takes the user_meat option as an argument. The purpose of the this function is an validation checker to enusre the meat option the user chooses is present within the csv file. If the user_meat entered is not alphabetical, the function identifies that as not a valid option and returns False. If the user_meat entered is alphabetical, the function opens the meats.csv file using the csv DictReader function. For row in reader, if row["name"] == user_meat, the function will recognise this as a valid option and return True.


#### get_meat
This function takes the user_meat option as an argument. It then opens the meats.csv file using the csv.DictReader function, for row in reader, if the name of the meat option matches the user_meat, the function then returns a dictionary to the main function with mulitple key-value pairs. The keys in the dictionary are the name of the meat + the nutritional values measured in this particular food group and the values are the nutritional values associated with that specific meat option found in the csv file.


### Databases
Contains .txt files of food groups. In each .txt file, names of options are unsorted.
