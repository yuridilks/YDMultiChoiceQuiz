"""
Base Component for NZ General Knowledge Quiz
v0 - skeleton setup
v1 - adding component one
v2 - adding component two
v3 - adding component four (not adding component three)
v4 - adding component five

Author - Yuri Dilks
CC YD 2022
"""
# importing 'ascii_lowercase' to allow my multi choice to be 'a', 'b', 'c'
from string import ascii_lowercase


# Functions go here ---------------------------------------------------------------------------------------------------
# creating a Yes / No Checker function to check users answers when answer the 'instruction' question
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


# created a Decorative Statement function for my program
def quiz_statements(statement, decoration):
    sides = decoration * 2
    statement = "{} {} {}".format(sides, statement, sides)
    decoration_border = decoration * len(statement)
# printing the 'decoration' around the statement
    print(decoration_border)
    print(statement)
    print(decoration_border)

    return ""


# created a Final Message function to print message to users at the end of the quiz
def final_message():
    # printing message to users if their score is in between 0 and 5
    if 0 < user_score <= 5:
        print("Good try, better luck next time!")
        return ""
    # printing message to users if their score is in between 6 and 8
    elif 6 < user_score <= 8:
        print("Great job!")
        return ""
    # printing message to users if their score is 9 or 10
    elif 9 < user_score <= 10:
        print("Amazing effort, well done!")
        return ""


# Main Routine goes here ----------------------------------------------------------------------------------------------
welcome_statement = "Welcome to the NZ General Knowledge Quiz!"
welcome_decoration = ":"
quiz_statements(welcome_statement, welcome_decoration)

# asking users if they have played the quiz before
played_quiz_before = yes_no_checker("Have you played this quiz before? ")

# printing instructions if users answer 'no'
if played_quiz_before == "no":
    print("~~~ How to Play the NZ General Knowledge Quiz ~~~")
    instruction_statement = "This quiz has 10 questions with multi-choice answers. You must choose the correct answer by entering 'a', 'b' or 'c'"
    instruction_decoration = "~"
    quiz_statements(instruction_statement, instruction_decoration)

QUIZ_QUESTIONS = {
    # creating a question and three answer options (in a list)
    "What is the capital city of New Zealand": [
        "Wellington", "Auckland", "Christchurch",
    ],
    "How many official languages are there in New Zealand": [
        "Three", "One", "Four",
    ],
    "What is New Zealand's official name in Maori": [
        "Aotearoa", "Kia Ora", "Aroha",
    ],
    "When was the Treaty of Waitangi signed": [
        "1840", "1860", "1940",
    ],
    "What is the name of the New Zealand's national rugby team": [
        "All Blacks", "Black Caps", "Tall Blacks",
    ],
    "What is the name of the largest lake in New Zealand": [
        "Lake Taupo", "Lake Wakatipu", "Lake Tekapo",
    ],
    "Which town in New Zealand can you find the 'Hobbiton' movie set": [
        "Matamata", "Dunedin", "Whanganui",
    ],
    "How many stars are on the New Zealand flag": [
        "Four", "Five", "Seven",
    ],
    "What does Aotearoa mean?": [
        "Land of the Long White Cloud", "Land of the Cloud", "Land of the Shiny White Cloud",
    ],
    "What is a 'hongi' in New Zealand": [
        "A traditional Maori greeting where people press their noses together", "A underground pit that cooks food with heated stones",
        "It can mean both of the above", ]
}
user_score = 0
# Created a 'for' loop for quiz questions
for number, (nz_question, answer_choices) in enumerate(QUIZ_QUESTIONS.items(), start=1):
    # printing what question it is (out of 10) - example: 'Question 1'
    print(f"\nQuestion {number}:")
    print(f"{nz_question}?")
    correct_answer = answer_choices[0]

    # using the imported 'ascii_lowercase' to label the answer choices
    labeled_option = dict(zip(ascii_lowercase, sorted(answer_choices)))
    for label, option in labeled_option.items():
        print(f"  {label}) {option}")
    # creating an 'error' message if users enter invalid answer
    while (answer_label := input("\nYour Answer: ")) not in labeled_option:
        print(f"Please answer 'a', 'b' or 'c' as your answer")

    answer = labeled_option[answer_label]
    if answer == correct_answer:
        # adding one point to the user's score
        user_score += 1
        # adding in the decoration statement to 'correct' answer
        correct_message = "Well done, that is CORRECT!"
        correct_decoration = "!"
        quiz_statements(correct_message, correct_decoration)
    # creating a print statement if the users answer incorrectly
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

    print(f"Your Current Score: {user_score} out of {number}\n")

# show the user's final score and called the final message function
final_statement = f"FINAL SCORE: {user_score} out of 10. {final_message()}"
final_decoration = "*"
quiz_statements(final_statement, final_decoration)
