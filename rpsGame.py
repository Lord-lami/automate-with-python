import random, sys

rps = ["rock", "paper", "scissors"]

usersMove = ""

wins, losses, ties = 0, 0, 0

print("ROCK, PAPER, SCISSORS")

while usersMove != "q":
    computersMove = random.choice(rps)
    
    print(wins, "Wins,", losses, "Losses,", ties, "Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    usersMove = input(">")
    
    winningMove = rps[(rps.index(computersMove) + 1) % 3]
    lossingMove = rps[rps.index(computersMove) - 1]

    
    if usersMove == computersMove[0]:
        ties += 1
        print(computersMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    elif usersMove == lossingMove[0]:
        losses += 1
        print(lossingMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    elif usersMove == winningMove[0]:
        wins += 1
        print(winningMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    else:
        sys.exit()
