"""
Yes No Checker
v1 - trialling ideas
v2 - improved version of the function

Author - Yuri Dilks
CC YD 2022
"""


# Functions go here ---------------------------------
# creating a yes / no checker function to check users answers when answer the 'instruction' question
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question)

        if user_response == "yes":
            return user_response

        elif user_response == "no":
            return user_response


# printing an 'error' message if user enters an answer that isn't 'yes' or 'no'
        else:
            print("Please answer this question with either a 'yes' or 'no' reply")


# Main Routine goes here ----------------------------
quiz_instructions = yes_no_checker("Have you played this quiz before? ")
