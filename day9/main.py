import os
clear = lambda: os.system('clear')

print("Welcome to the secret auction.")

no_bidders = False
bidders = {}
while not no_bidders:
    bidder_name = input("What is your name: ")
    bidder_bid  = input("What is your bid? $")

    bidders[bidder_name] = bidder_bid

    more_bidders = input("Are there any more bidders? ('yes' or 'no') ")

    clear()

    if more_bidders == "no":
        no_bidders = True

highest_bidder = max(bidders, key=bidders.get)

print(f"{highest_bidder} has the highest bid of ${bidders[highest_bidder]}")