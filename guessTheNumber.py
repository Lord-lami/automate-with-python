import random

theNumber = random.randint(1, 20)

guess = 0

attempts = 1

print("I am thinking of a number between 1 and 20")

while attempts < 8:
    print("Take a guess")
    guess = int(input(">"))
    if guess < theNumber:
        print("Your guess is too low")
    elif guess > theNumber:
        print("Your guess is too high")
    else:
        break
    attempts += 1

if guess == theNumber:
    print("Good job! You got it in", attempts, "guesses")
else:
    print("You failed! The number was", theNumber)