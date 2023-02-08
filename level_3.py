guess = 0
player = int(input("Pick a number 1-10? "))
computer = 0
low = 1
high = 10

while computer != player:
    # could also say while True:
    guess += 1
    computer = (low + high) // 2

    if computer > player:
        print("Computer guessed", computer, "Too high."
              "This is guess number", guess,)
        high = computer - 1
        continue
    elif computer < player:
        print("Computer guessed", computer, "Too low."
              "This is guess number", guess,)
        low = computer + 1
        continue
if computer == player:
    print("Computer guessed", computer, "Computer wins! :)",
          "This is guess number", guess)
