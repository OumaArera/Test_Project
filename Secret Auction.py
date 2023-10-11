#Welcoming to the Auction
print("\nWelcome to the Secret Auction")

#create empty dictionary for my_dict and empty list for bids
my_dict = {}
bids = []

#We set the bid_on to true
#To check if the bid is still continue
bid_on = True

#We create a loop to ensure the bidding continues
while bid_on:

    #Game start with the next bidder
    next_bidder = input("\nIs there another bidder? Type Y or N ").lower()



    #if response of next_bidder is y or yes then the game continues
    if next_bidder == "y" or next_bidder == "yes":

        name = input("\nWhat is your name? ")
        bid = int(input("\nEnter your bid "))

        #Add bid to the list bids
        bids.append(bid)

        #Add key = name and value = bid to my_dict
        my_dict[name] = bid

    #In case the next_bidder says anything other than y or yes
    #Then bid_on is False
    else:
        bid_on = False
        print("\nEnd of game!")

        #Check for the highest bid in the bids list
        highest_bid = max(bids)

        #checking if the highest value in the dictionary is equal to the highest value in bids
        #In that case we print the key and value
        for key in my_dict:
            if my_dict[key] == highest_bid:  # check if the bid in the dictionary matches the highest bid
                print(f"\nWinner is {key} who's bid is {highest_bid}.")
