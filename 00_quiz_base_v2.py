"""
Base Component for NZ General Knowledge Quiz
v0 - skeleton setup
v1 - adding component one
v2 - adding component two

Author - Yuri Dilks
CC YD 2022
"""
# Functions go here ---------------------------------


# Yes / No Checker function
# creating a yes / no checker function to check users answers when answer the 'instruction' question
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        # if users have played quiz before, program continues
        if user_response == "y" or user_response == "yes":
            user_response = "yes"
            return user_response

        # if users haven't played quiz before, show instructions
        elif user_response == "n" or user_response == "no":
            user_response = "no"
            return user_response

        # printing a statement if user answers invalid input
        else:
            print("Please enter a 'yes' or 'no' answer")


# Instruction function
# creating easy-to-read instructions for users if they haven't played the game before
def quiz_instruction():
    print()
    print("~~~ How to Play the NZ General Knowledge Quiz ~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("This quiz has multi-choice answers. You must choose the correct answer by entering 'a', 'b' or 'c'")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return ""


# Main Routine goes here --------------------------
# asking users if they have played the quiz before
played_quiz_before = yes_no_checker("Have you played this quiz before? ")

# printing instructions if users answer 'no'
if played_quiz_before == "no":
    quiz_instruction()

print("Program Continues")
