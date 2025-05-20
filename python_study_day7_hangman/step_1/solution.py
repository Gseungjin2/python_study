from main import word_list
import random

chosen_word = random.choice(word_list)

print(chosen_word)

dispay_holder = ['_'] * len(chosen_word) 

print(''.join(dispay_holder))

guess = input("Guess a letter:").lower()

for index, letter in enumerate(chosen_word):
    if letter == guess:
        dispay_holder[index] = letter

updated_dispay_holder = ''.join(dispay_holder)

print(updated_dispay_holder)
        



           

