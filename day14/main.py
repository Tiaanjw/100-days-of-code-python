import random
from game_art import LOGO, VS
from game_data import GAME_DATA
import os
clear = lambda: os.system('clear')

print(LOGO)

def check_answer(user_choice, followers_a, followers_b):
    if followers_a > followers_b:
        return user_choice == "a"
    else:
        return user_choice == "b"

def run_game():
    score = 0
    while True:    
        random_choice_idx_1 = random.randint(0, len(GAME_DATA) - 1)
        new_game_data = list(GAME_DATA)
        
        del new_game_data[random_choice_idx_1]

        choice_1 = GAME_DATA[random_choice_idx_1]
        choice_2 = random.choice(new_game_data)

        print(f"Compare A: {choice_1['name']}, {choice_1['description']}, {choice_1['country']}")
        print(VS)
        print(f"Compare B: {choice_2['name']}, {choice_2['description']}, {choice_2['country']}")

        user_choice = input("Who has more followers? (a/b): ")

        clear()

        if check_answer(user_choice, int(choice_1['follower_count']), int(choice_2['follower_count'])):
            score += 1
        else:
            print(f"A: {choice_1['name']}, followers: {choice_1['follower_count']}")            
            print(f"B: {choice_2['name']}, followers: {choice_2['follower_count']}")   
            print(f"You lose, your score: {score}")
            return
        
        print(f"You're right!, Current Score: {score}")
        


while True:
    start = input("Would you like to play a game? (y/n) \n")
    if start == "n":
        exit()

    clear()

    run_game()
    