bidders ={

}


def find_winner():
    highest_bid = 0
    highest_bid_name = ""
    for participant in bidders:
        if bidders[participant] > highest_bid:
            highest_bid = bidders[participant]
            highest_bid_name = participant
    print(f"The winner is {highest_bid_name} with a bid of {highest_bid}$!")



end_status = False
while not end_status:
    name = input("What's the bidder's name?\n")
    bid = int(input("Enter bid amount\n"))
    bidders[name] = bid
    add_bidder = input("Add another bidder?\n").lower()
    if add_bidder == "no" or add_bidder == "n":
        end_status = True
        find_winner()
    elif add_bidder != "yes" or add_bidder != "y":
        break
    else:
        print("Error")
# ToDo - check figure out why the thing outputs "Error" unconditionally
# Fix: just add a break() lol