import random

guess = 0
player = int(input("Pick a number 1-10 "))


while guess < 3:
    guess += 1
    computer = random.randint(1, 10)

    if computer == player:
        print("The computer wins! ")
        break
    elif computer < player:
        print("The computer guess is too low.")
    else:
        print("The computer guess is too high.")

    if guess == 3:
        print("The computer ran out of guesses. You win. :)")
        print("the number was", player)
