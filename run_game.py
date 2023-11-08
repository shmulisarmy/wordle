from colorama import Fore
from wordle_answer_alphabetical import five_letter_words
import random

word = random.choice(five_letter_words)
guess_number = 0

with open('store_new_words.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        five_letter_words.append(line[:-1:])

while True:
    guess = input('\nfive letter_index word: ')
    
    if len(guess) != 5:
        print('not five letters')
        continue
    if guess not in five_letter_words:
        print('not vallid word')
        with open('store_new_words.txt', 'a') as file:
            file.write(f'\n{guess}')
        continue

    guess_number += 1

    if guess == word:
        print(Fore.GREEN + guess + Fore.RESET)
        print(f'you won in {guess_number} guesses')
        break
    for letter_index in range(len(guess)):
        if word[letter_index] == guess[letter_index]:
            print(Fore.GREEN + guess[letter_index], end = Fore.RESET)
        elif guess[letter_index] in word:
            print(Fore.YELLOW + guess[letter_index], end = Fore.RESET)
        else:
            print(guess[letter_index], end = '')