# -------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# -------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# -------------------------

questions = {
    "If you freeze water, what do you get?": "A",
    "How many legs does a spider have?": "C",
    "What is the colour of and emerald": "A",
    "How many planets are in our solar system?": "B",
    "What year was Python created?": "B",
    "Who created Python?": "A",
    "Python is tributed to which comedy group?": "C",
    "Is the Earth round?": "A"
}

options = [["A.Ice", "B.Water", "C.Smoke", "D.Fire"],
           ["A.6", "B.4", "C.8 ", "D.9"],
           ["A.Green", "B.Red", "C.Black", "D.Orange"],
           ["A.10", "B.8", "C.12", "D.6"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016",],
           ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()

while play_again():
    new_game()

print("Bye!")

# -------------------------
