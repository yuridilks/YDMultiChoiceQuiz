# Functions go here ------------------------------
# Version 2 - turned into function

def number_check(rounds_question, too_low, too_high):
    error_message = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # Ask the user how many rounds they would like to play
            user_response = int(input(rounds_question))

            # If user enters number lower than 1 or higher than 10
            if too_low < user_response <= too_high:
                return user_response

            else:
                print(error_message)

        except ValueError:
            print(error_message)


# Main Routine goes here -------------------------
how_many_rounds = number_check("How many rounds of the quiz would you like to play? ", 0, 10)
print("You will be playing {} rounds of this quiz".format(how_many_rounds))
