"""
Quiz Questions
v1 - trial (no functions)
v2 - turned questions into function and list
v3 - improved the component
v4 - finalised this component

Author - Yuri Dilks
CC YD 2022
"""
# importing 'ascii_lowercase' to allow my multi choice to be 'a', 'b', 'c'
from string import ascii_lowercase
# Functions go here ------------------------------------

# Main Routine goes here -------------------------------
QUIZ_QUESTIONS = {
    "What is the capital city of New Zealand": [
        "Wellington",
        "Auckland",
        "Christchurch",
    ],
    "How many official languages are there in New Zealand": [
        "Three",
        "One",
        "Four",
    ],
    "What is New Zealand's official name in Maori": [
        "Aotearoa",
        "Kia Ora",
        "Aroha",
    ],
    "When was the Treaty of Waitangi signed": [
        "1840",
        "1860",
        "1940",
    ],
    "What is the name of the New Zealand's national rugby team": [
        "All Blacks",
        "Black Caps",
        "Tall Blacks,"
    ],
    "What is the name of the largest lake in New Zealand": [
        "Lake Taupo",
        "Lake Wakatipu",
        "Lake Tekapo",
    ],
    "Which town in New Zealand can you find the 'Hobbiton' movie set": [
        "Matamata",
        "Dunedin",
        "Whanganui",
    ],
    "How many stars are on the New Zealand flag": [
        "Four",
        "Five",
        "Seven",
    ],
    "What does Aotearoa mean?": [
        "Land of the Long White Cloud",
        "Land of the Cloud",
        "Land of the Shiny White Cloud",
    ],
    "What is a 'hongi' in New Zealand": [
        "A traditional Maori greeting where people press their noses together",
        "A underground pit that cooks food with heated stones",
        "It can mean both of the above",
    ]
}

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

    # having a line where users can enter their answer
    answer_label = input("\nYour Answer: ")
    answer = labeled_option.get(answer_label)
    if answer == correct_answer:
        print("Well done, that is correct!")

    # creating a print statement if the users answer incorrectly or enter an invalid answer
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
