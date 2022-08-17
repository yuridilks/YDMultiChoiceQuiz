"""
Base Component for NZ General Knowledge Quiz
v0 - skeleton setup
v1 - adding component one
v2 - adding component two

Author - Yuri Dilks
CC YD 2022
"""


# Functions go here ---------------------------------
# creating a yes / no checker function to check users answers when answer the 'instruction' question
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        # if users have played quiz before, program continues
        if user_response == "y" or user_response == "yes":
            user_response = "yes"
            print("Program Continues")
            return user_response

        # if users haven't played quiz before, show instructions
        elif user_response == "n" or user_response == "no":
            user_response = "no"
            print("Show Instructions")
            return user_response

        # printing a statement if user answers invalid input
        else:
            print("Please enter a 'yes' or 'no' answer")


# Main Routine goes here ----------------------------
# asking users if they have played the quiz before
quiz_instructions = yes_no_checker("Have you played this quiz before? ")
print("You answered {} to playing this quiz before".format(quiz_instructions))
