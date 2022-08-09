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
    print("~~~ How to Play the NZ General Knowledge Quiz ~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("This quiz has multi-choice answers. You must choose the correct answer by entering 'a', 'b' or 'c'")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return ""


# Main Routine goes here --------------------------
played_quiz_before = yes_no_checker("Have you played this quiz before? ")

if played_quiz_before == "no":
    quiz_instruction()

print("Program Continues")
