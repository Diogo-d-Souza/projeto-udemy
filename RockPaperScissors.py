import random
import time
print("Lets play a game very known here! rock, paper and scissors.")

player = input('''To start the game, you must choose one of three opttions below to duel the computer:
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SO, WHICH ONE WILL YOU CHOOSE?
''')
time.sleep(1)

if player.lower() == "rock":
    print('''You choose ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
    time.sleep(1.5)
elif player.lower() == "paper":
    print('''You choose PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    time.sleep(1.5)
elif player.lower() == "scissors":
    print('''You choose scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    time.sleep(1.5)
else:
    print("You wrote something wrong")


computer = random.randint(1,3)
if computer == 1:
    print('''Computer choose ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    ''')
elif computer == 2:
    print('''Computer choose PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
else:
    print('''Computer choose SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')


if player.lower() == "rock" and computer == 1:
    print("Draw!")
elif player.lower() == "rock" and computer == 2:
    print("The computer wins, good luck next time!")
elif player.lower() == "rock" and computer == 3:
    print("You win!")

elif player.lower() == "paper" and computer == 1:
    print("You win!")
elif player.lower() == "paper" and computer == 2:
    print("Draw!")
elif player.lower() == "paper" and computer == 3:
    print("The computer wins, good luck next time!")

elif player.lower() == "scissors" and computer == 1:
    print("The computer wins, good luck next time!")
elif player.lower() == "scissors" and computer == 2:
    print("You win!")
elif player.lower() == "scissors" and computer == 3:
    print("Draw!")

