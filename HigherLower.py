from dataHigherLowergame import data
from random import randint

user_try = True
score = 0
famous_b = data[randint(0, 49)]

while user_try:
    famous_a = famous_b
    famous_b = data[randint(0, 49)]
    if famous_a == famous_b:
        famous_b = data[randint(0, 49)]

    followers_1 = famous_a["follower_count"]
    followers_2 = famous_b["follower_count"]

    compare = ""
    if followers_1 > followers_2:
        compare = "a"
    else:
        compare = "b"

    print(f"Compare A: {famous_a['name']}, a {famous_a['description']}, from {famous_a['country']}")
    print(f"Against B: {famous_b['name']}, a {famous_b['description']}, from {famous_b['country']}")
    user_choice = input("Who has more followers? type 'A' or 'B': ")
    if user_choice.lower() == compare:
        score += 1
        print(f"Your score is {score}")
    else:
        print(f"Wrong answer, your final score is {score}")
        user_try = False


