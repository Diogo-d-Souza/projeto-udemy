from random import randint

attempts_hard = 5
attempts_easy = 10

def difficulty():
    dif = input("Choose a difficulty. 'hard' or 'easy'\n")
    if dif == "hard":
        return attempts_hard
    else:
        return attempts_easy


def number(number, number_generator, attempts):
    if number < number_generator:
        print("Too low.")
        return attempts - 1
    elif number > number_generator:
        print("Too high.")
        return attempts - 1
    else:
        print("You got it the answer is {}".format(number_generator))


def game():
    print("The computer is thinking one number between 1 and 100. Try to guess which number is!")
    number_generator = randint(1, 10)
    attempts = difficulty()
    attempt_user = 0
    while attempt_user != number_generator:
        print("You have {} attempts to try.".format(attempts))
        attempt_user = int(input("Guess a number: "))
        attempts = number(attempt_user, number_generator, attempts)
        if attempts == 0:
            print("Your attempts is over. Game over")
            return
        elif attempt_user != number_generator:
            print("Guess again")

game()
