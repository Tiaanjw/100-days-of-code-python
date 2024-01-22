import random
import os
clear = lambda: os.system('clear')

print("""
   ____                       _   _                                  _               _ _ _ 
  / ___|_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __| | | |
 | |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| | | |
 | |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  |_|_|_|
  \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_|_|_)\n
""")

number_start = 0
number_end   = 100

def get_random_number(start, end):
    return random.randint(start, end)

def run_game(user_lives):
    number = get_random_number(number_start, number_end)
    print(f"I'm thinking of a number between {number_start} and {number_end}")

    while user_lives > 0:
        guess = int(input("What is your guess: "))
        user_lives -= 1
        
        if guess == number:
            print("You guessed right!!!")
            return
        elif guess > number:
            print(f"Too high, lives: {user_lives}")
        elif guess < number:
            print(f"Too low, lives: {user_lives}")
    
    print(f"You have lost, the number was {number}")
    return


while True:
    start = input("Would you like to play a game? (easy/hard/exit) \n")
    if start == "exit":
        exit()

    if start == "hard":
        user_lives = 5
    elif start == "easy":
        user_lives = 10

    clear()
    
    print(f"You have {user_lives} attempts to guess the right number, good luck!")

    run_game(user_lives)