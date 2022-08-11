# Functions go here ---------------------------------

# Main Routine goes here ----------------------------

error_message = "Please enter a whole number between 1 and 10"

valid = False
while not valid:
    try:
        # Ask the user how many rounds they would like to play
        user_response = int(input("How many rounds of the quiz would you like to play? "))

        # If user enters number lower than 1 or higher than 10
        if 0 < user_response <= 10:
            print("You have chosen to play {} rounds of the quiz".format(user_response))

        else:
            print(error_message)

    except ValueError:
        print(error_message)
