#Hangman

import random
import os
from hangman_art import hangman_logo, hangman_stages
from hangman_words import hangman_words

clear = lambda: os.system('clear')

lives = 6

word_list = hangman_words
random_word = random.choice(word_list)
fill_in_word = []
for letter in random_word:
    fill_in_word.append("_")

clear()
while lives > 0:
    print(hangman_logo)
    print(f"Lives: {lives}")
    print(hangman_stages[lives])
    print(f"Welcome to hangman, your word has {len(random_word)} characters")
    print("".join(fill_in_word))
    user_char = input("Guess a character: ").lower()[0]
    
    clear()

    if user_char in fill_in_word:
        print(f"You have already guessed {user_char}")
        continue
  
    char_found = False
    for idx in range(0, len(random_word)):
        if random_word[idx] == user_char:
            fill_in_word[idx] = user_char
            char_found = True

    if not char_found:
        lives -= 1
        
    fill_in_word_str = "".join(fill_in_word)
    
    if fill_in_word_str == random_word:
        print("You win!!!")
        exit()

print(f"You lose, your word was {random_word}, better luck next time...")
