import time
print("Welcome to Black Mirror Game")
print(40 * "-=-=")
time.sleep(1)
start = input("If you want star the game, press enter ")
print(40 * "-=-=")
time.sleep(1.5)

if start == "":
  print("You're about to begin the game, get ready!")
  print(40 * "-=-=")
  time.sleep(1)
  choose_1 = input("First, you're in a cave and need to choose between go to the right or left, so which one will you choose ('right'/'left')? ")
  print(40 * "-=-=")
  time.sleep(1)
  if choose_1.lower() == "left":
    print("Unfortunately you choose the worst way, you fell into a hole and die")
  elif choose_1.lower() == "right":
    choose_2 = int(input('''That's the way! Go on and good luck with your choices, be careful
Now you have to think a little, use your knowledge in math and solve this problem: (3 x 6) + 6 / 2**2
Your answer: '''))
    time.sleep(1)
    print(40 * "-=-=")
    if choose_2 == 3:
      choose_3 = input('''Great! you are in the homestretch, one more question and you'll win the game!
You have 2 pills, the blue and the red one, and you have to choose between one of this. 
The blue pill will make you know all the truth about this cave, and why you are there
The red pill will take you out of this cave and you'll be safe
Wich one do you choose (B/R)? ''')
      time.sleep(2)
      if choose_3.lower() == "b":
        print("You are the chosen one! Congratulations, Neo")
      else:
        print("You've chosen the easiest way, you'll never know what was given to you and what the future will provide you!")
    else:
      print("The right answer is 3, try again next time")
  else:
    print("You wrote something wrong")
else:
  print("See you next time!")


