"""
Quiz Instructions
v1 - first version (longer instruction message)
v2 - improved version of the component (shorter, refined version of the instructions)

Author - Yuri Dilks
CC YD 2022
"""

# Functions go here ---------------------------------


# Yes / No Checker function
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        if user_response == "y" or user_response == "yes":
            user_response = "yes"
            return user_response

        elif user_response == "n" or user_response == "no":
            user_response = "no"
            return user_response

        else:
            print("Please enter a 'yes' or 'no' answer")


# Instruction function
def quiz_instruction():
    print("*** How to Play the NZ General Knowledge Quiz ***")
    print("This game is a multiple choice quiz that is based on NZ General Knowledge. "
          "You must answer the question with what you believe is the right answer, by entering 'a', 'b' or 'c'."
          "Good luck!")
    return ""


# Main Routine goes here --------------------------
# asking the user if they have played the quiz before
played_quiz_before = yes_no_checker("Have you played this quiz before? ")

if played_quiz_before == "no":
    quiz_instruction()

print("Program Continues")
