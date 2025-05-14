from main import word_list
import random

chosen_word = random.choice(word_list)
print(chosen_word)
user_choice = input(str("Guess a letter:"))

for user_choice_letter in chosen_word:
    if user_choice_letter == user_choice:
        print("Right")
    else:
        print("Wrong")