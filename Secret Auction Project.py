# Importing an art module and print the logo variable 
import Auction_Image
print(Auction_Image.logo)
# Welcoming people for the auction
print("Welcome to the secret auction program")

# Created a Function to get the Highest bidder 
def find_highest_bidder(Auction):
    Winner = "" 
    High_bid = 0

    max(Auction)
    for bids in Auction:
        bid_amount = Auction[bids]# Created bid_amount to store the values of bids
        if bid_amount > High_bid: # Using the if to get the Highest bid from the Auction dictionary
            High_bid = bid_amount
            winner = bids
        elif bid_amount == High_bid: # Used elif to see if its draw
            print(f"Its draw the bid is {High_bid}")

# Creating a empty dictionary called Auction
Auction ={}

Game_over = True
# Used while for asking if there is any other bidders 
while Game_over:
    name = input("What is your name?:").lower()
    Bid = int(input("Please a enter a bid number:"))
    Auction[name] = Bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no.").lower()
    if continue_bid == 'no':
        Game_over = False
        find_highest_bidder(Auction)
    elif continue_bid == 'yes':
        print("\n"*30)



