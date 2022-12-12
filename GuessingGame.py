import random

number = random.randint(1,10)
# can cheat by adding "print(number)"

print("You have three tries to guess the random number between 1 and 10")
guess = input("Guess: ")

i = 1
while int(guess) != number:
    guess = input("Guess again: ")
    i = i + 1
    if i == 3:
        break

if int(guess) == number:
    print("You won!")

if int(guess) != number:
    print("You lose!")
