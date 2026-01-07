bids={}
continue_bidding =True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is you bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)