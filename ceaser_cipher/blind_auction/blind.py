import os
import art

print(art.logo)
print("Welcome to the secret auction program.")



def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        os.system('clear')
        
        


        
    
    




