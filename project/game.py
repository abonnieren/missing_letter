import random

from random_word import RandomWords

import get_emoji_based_on_result as e
import answer_checker as a
import integer_input as i

r = RandomWords()

random_word = ""
missing_letter = ""

score = 0
question_number = 0


def askQuestion():
    global random_word
    global missing_letter
    global question_number
    random_word = ""
    missing_letter = ""
    random_word = r.get_random_word()
    letters = []
    for l in random_word:
        letters.append(l)

    missing_index = random.randint(0,len(letters)-1)
    missing_letter = letters[missing_index]
    for i in range(len(letters)):
        if i == missing_index:
            letters[i] = "_"

    q_word = "".join(letters)
    if question_number == 0:
        print("\n")
        print("Quiz is start.\nYou'll get 3 chances to answer each question.\nFor each correct answer 1 mark will be added(+) and for each wrong answer 0.25 mark will be subducted(-).\nBest of luck 🤞")
        print("\n")
    print(f"Q{question_number + 1}. Guess the missing letter of: {q_word}")
    question_number += 1


total_questions = i.get_integer_input("How many question do you want to answer? ")

while question_number <= total_questions:
    try_number = 0
    if question_number == total_questions:
        print("Quiz is over!")
        print("\n")
        print(f"Your score: {score}/{total_questions} {e.get_emoji(score,total_questions)}")
        break
    askQuestion()
    while try_number <= 3:
        if try_number == 3:
            print(f"The correct answer was {missing_letter}")
            if question_number != total_questions:
                print("Try next one")
            print("\n")
            try_number = 0
            break
        answer = input("> ")
        if a.answerChecker(answer,missing_letter):
            print("Correct!")
            print("\n")
            try_number = 0
            score += 1
            break
        else:
            print("Wrong")
            try_number += 1
            score -= 0.25