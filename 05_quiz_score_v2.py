"""
Quiz Score
v1 - created a function and score
v2 - another function for 'final score'

Author - Yuri Dilks
CC YD 2022
"""
# importing 'ascii_lowercase' to allow my multi choice to be 'a', 'b', 'c'
from string import ascii_lowercase


# Functions go here ---------------------------------------------------------------------
# created a decoration statement function for my program
def quiz_statements(statement, decoration):
    sides = decoration * 2
    statement = "{} {} {}".format(sides, statement, sides)
    decoration_border = decoration * len(statement)

# printing the 'decoration' around the statement
    print(decoration_border)
    print(statement)
    print(decoration_border)

    return ""


# created a decoration statement to show the user's final score
def question_border(statement, decoration):
    statement = "{}".format(statement)
    decoration_line = decoration * len(statement)

    print(decoration_line)
    print(statement)
    print(decoration_line)

    return ""


# Main Routine goes here ----------------------------------------------------------------
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
        "All Blacks", "Black Caps", "Tall Blacks,"
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
        "It can mean both of the above",
    ]
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
        correct_decoration = "-"
        quiz_statements(correct_message, correct_decoration)
        print(f"Your Current Score: {user_score} out of {number}")

    # creating a print statement if the users answer incorrectly
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        print(f"Your Current Score: {user_score} out of {number}")

# show the user's final score
final_statement = f"FINAL SCORE: {user_score} out of 10"
final_decoration = "*"
question_border(final_statement, final_decoration)
