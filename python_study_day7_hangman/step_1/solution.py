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

print(type(updated_dispay_holder))
        

     
'''
강의 영상 답안
'''
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter:").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
