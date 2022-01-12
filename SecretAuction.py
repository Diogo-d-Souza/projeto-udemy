from replit import clear

bids = {}

end_of_bid = False

while not end_of_bid:

    user_key = input("What is your name?\n")
    user_value = int(input("what is your bid(only integer numbers)?\n"))
    bids[user_key] = user_value
    request = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if request.lower() == "no":
        end_of_bid = True
    elif request.lower() == "yes":
        clear()

highest = 0
for key in bids:
    if bids[key] > highest:
        highest = bids[key]
        winner = key
print("The winner is {} with a bid of {}$".format(winner, highest))


