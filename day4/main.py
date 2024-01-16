import random

print("Rock, Paper, Scissors!")

user_input = int(input("Input required: (0 = rock, 1 = paper, 2 = scissors)\n"))
game_map = ["Rock", "Paper", "Scissors"]
computer_input = random.randint(0,2)
user_wins = False
draw = False

if user_input == 0 and computer_input == 2:
  user_wins = True
elif user_input == 1 and computer_input == 0:
  user_wins = True
elif user_input == 2 and computer_input == 1:
  user_wins = True
elif user_input == computer_input:
  draw = True

if draw:
  print(f"You chose {game_map[user_input]} and the computer draw {game_map[computer_input]}, it is a draw...")
elif user_wins:
  print(f"You chose {game_map[user_input]} and the computer draw {game_map[computer_input]}, you win!!!")
else:
  print(f"You chose {game_map[user_input]} and the computer draw {game_map[computer_input]}, computer wins :(")