#Blackjack

import random
import os
clear = lambda: os.system('clear')

cards_map = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def player_wins(player_cards, computer_cards):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* YOU WIN *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"You win!! cards: {player_cards}, total: {get_cards_sum(player_cards, cards_map)}")
    print(f"Computer loses: {computer_cards}, total: {get_cards_sum(computer_cards, cards_map)}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")    

def computer_wins(player_cards, computer_cards):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-* COMPUTER WINS *-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Computer wins: {computer_cards}, total: {get_cards_sum(computer_cards, cards_map)}")
    print(f"Your cards: {player_cards}, total: {get_cards_sum(player_cards, cards_map)}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def game_draw(player_cards, computer_cards):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* DRAW *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Computer Cards: {computer_cards}, total: {get_cards_sum(computer_cards, cards_map)}")
    print(f"Your cards: {player_cards}, total: {get_cards_sum(player_cards, cards_map)}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def draw_new_card(cards_map):
    return random.choice(list(cards_map.keys()))

def get_cards_sum(cards, cards_map):
    cards_values = []
    for card in cards:
        cards_values.append(cards_map[card])

    if sum(cards_values) > 21:
        if 11 in cards_values:
            idx = cards_values.index(11)
            cards_values[idx] = 1

    return sum(cards_values)
    
while True:
    player_lost = False
    computer_lost = False
    player_cards_index = []
    player_cards = []
    computer_cards = []

    playing_input = input("Would you like to play a game of blackjack? (y/n)")
    clear()
    if playing_input != "y":
        exit()

    for _ in range(2):
        player_cards.append(draw_new_card(cards_map))
        computer_cards.append(draw_new_card(cards_map))

    print(f"Your cards {player_cards}, computer's first card [{computer_cards[0]}]")

    while True:
        hit = input("Would you like another card? (y/n)")
        if hit != "y":
            break

        draw_card = draw_new_card(cards_map)
        print(f"You draw {draw_card}")
        player_cards.append(draw_card)

        player_total = get_cards_sum(player_cards, cards_map)

        if player_total > 21:
            player_lost = True
            break
        
        print(f"Your cards: {player_cards}, total: {player_total}")
        
    if not player_lost:
        while True:
            should_draw = random.choice([True, False])
            computer_total = get_cards_sum(computer_cards, cards_map)

            if computer_total < 21:
                if should_draw:
                    draw_card = draw_new_card(cards_map)
                    computer_cards.append(draw_card)

                    computer_total = get_cards_sum(computer_cards, cards_map)

                    if computer_total > 21:
                        computer_lost = True
                        break
                else:
                    break
    else:
        computer_wins(player_cards, computer_cards)
        continue

    if not computer_lost:
        player_total = get_cards_sum(player_cards, cards_map)
        computer_total = get_cards_sum(computer_cards, cards_map)

        if player_total == computer_total:
            game_draw(player_cards, computer_cards)
        elif player_total > computer_total:
            player_wins(player_cards, computer_cards)
        elif player_total < computer_total:
            computer_wins(player_cards, computer_cards)
    else:
        player_wins(player_cards, computer_cards)