import random, pymsgbox

theNumber = random.randint(1, 20)

guess = 0

attempts = 1

pymsgbox.alert("I am thinking of a number between 1 and 20")

while attempts < 8:
    guess = int(pymsgbox.prompt("Take a guess"))
    if guess < theNumber:
        pymsgbox.alert("Your guess is too low")
    elif guess > theNumber:
        pymsgbox.alert("Your guess is too high")
    else:
        break
    attempts += 1

if guess == theNumber:
    pymsgbox.alert(f"Good job! You got it in {attempts} guesses")
else:
    pymsgbox.alert(f"You failed! The number was {theNumber}")
