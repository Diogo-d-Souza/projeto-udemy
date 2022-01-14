import random as rd
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def random_pick():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card

def is_blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, pc):
    if user == pc:
        return "Draw"
    elif pc == 0:
        return "The computer win with a Blackjack"
    elif user == 0:
        return "You win with a Blackjack"
    elif user > 21:
        return "You went over 21 points, you lose"
    elif pc > 21:
        return "PC went over 21 points, you win"
    elif user > pc:
        return "You win"
    elif pc > user:
        return "You lose"


def play_game():
    user_cards = [random_pick(), random_pick()]
    pc_cards = [random_pick(), random_pick()]
    end_of_game = False

    print(logo)

    while not end_of_game:

        user_sum = is_blackjack(user_cards)
        pc_sum = is_blackjack(pc_cards)
        print(f"Your cards {user_cards}, currently score {user_sum}")
        print(f"PC first card {pc_cards[0]}")

        if user_sum == 0 or pc_sum == 0 or user_sum > 21:
            end_of_game = True
        else:
            another_card = input("do you want to pick another card? type 'y' or 'n'.\n")
            if another_card == "y":
                user_cards.append(random_pick())
            else:
                end_of_game = True

    while pc_sum != 0 and pc_sum < 17:
        pc_cards.append(random_pick())
        pc_sum = is_blackjack(pc_cards)

    print(f"Your final cards {user_cards}, currently score {user_sum}")
    print(f"PC final cards {pc_cards}, currently score {pc_sum}")
    print(compare(user_sum, pc_sum))

while input("Do you want to play BlackJack game? type 'y' or 'n'. ") == "y":
    clear()
    play_game()