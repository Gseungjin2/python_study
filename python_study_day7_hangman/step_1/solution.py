from main import word_list
import random

chosen_word = random.choice(word_list)

print(chosen_word)

display_holder = ['_'] * len(chosen_word) 

print(''.join(display_holder))

# TOOD-1: - Use a while loop to let the user again.
gaem_over = False

while not gaem_over:
    guess = input("Guess a letter:").lower()
    

#TOOD-2: - Change the for loop so that you keep the previous correct guesses.

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display_holder[index] = letter

updated_dispay_holder = ''.join(display_holder)

print(updated_dispay_holder)
        

     
'''
강의 영상 답안
'''
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)

# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# TOOD-1: - Use a while loop to let the user again.

# guess = input("Guess a letter:").lower()

# display = ""

#TOOD-2: - Change the for loop so that you keep the previous correct guesses.

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)
