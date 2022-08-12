"""
Base Component for NZ General Knowledge Quiz
v0 - skeleton setup
v1 - added component one

Author - Yuri Dilks
CC YD 2022
"""


# Functions go here ---------------------------------
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        if user_response == "y" or user_response == "yes":
            user_response = "yes"
            print("Program Continues")
            return user_response

        elif user_response == "n" or user_response == "no":
            user_response = "no"
            print("Show Instructions")
            return user_response

        else:
            print("Please enter a 'yes' or 'no' answer")


# Main Routine goes here ----------------------------

quiz_instructions = yes_no_checker("Have you played this quiz before? ")
print("You answered {} to playing this quiz before".format(quiz_instructions))
