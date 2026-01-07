bids={}
continue_bidding =True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is you bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")