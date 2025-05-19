from main import word_list
import random

chosen_word = random.choice(word_list)

print(chosen_word)

dispay_holder = '_' * len(chosen_word) 

print(dispay_holder)

guess = input("Guess a letter:").lower()

for letter in chosen_word:
    if letter == guess:
        
           

print(dispay_holder)