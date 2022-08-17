# Functions go here ------------------------------------


# Main Routine goes here -------------------------------
# Question One
# asking the user the question
user_answer = input("What is the capital city of New Zealand? ")
# creating a 'correct' statement if users answer correctly
if user_answer == "Wellington":
    print("Well done, that is correct!")

# printing a statement if users enter invalid or incorrect answer
else:
    print("Sorry, that is incorrect. The answer is 'Wellington', not {}.".format(user_answer))

# Question Two
user_answer = input("How many official languages are there in New Zealand? ")
if user_answer == "Three":
    print("Well done, that is correct!")
else:
    print("Sorry, that is incorrect. The answer is 'Three', not {}.".format(user_answer))

# Question Three
user_answer = input("What is New Zealand's official name in Maori ")
if user_answer == "Aotearoa":
    print("Well done, that is correct!")
else:
    print("Sorry, that is incorrect. The answer is 'Aotearoa', not {}.".format(user_answer))
