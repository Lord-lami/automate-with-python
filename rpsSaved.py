import random, sys, shelve, dbm

print("ROCK, PAPER, SCISSORS")

record_exists = False

try:
    with shelve.open("rpsData", flag="r"):
        record_exists = True
except dbm.error:
    record_exists = False

wins, losses, ties = 0, 0, 0

if record_exists:
    print("Type \"n\" for New Game")
    print("Type anything else to Continue")
    new_game = input()
    if new_game.lower() != "n":
        with shelve.open("rpsData") as rpsData:
            wins = rpsData["wins"]
            losses = rpsData["losses"]
            ties = rpsData["ties"]

def updateRpsData():
    with shelve.open("rpsData") as rpsData:
        global wins, losses, ties
        rpsData["wins"] = wins
        rpsData["losses"] = losses
        rpsData["ties"] = ties
    print("Your stats are saved!")

rps = ["rock", "paper", "scissors"]

usersMove = ""

while usersMove != "q":
    computersMove = random.choice(rps)
    
    print(wins, "Wins,", losses, "Losses,", ties, "Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    usersMove = input(">")
    
    winningMove = rps[(rps.index(computersMove) + 1) % 3]
    lossingMove = rps[rps.index(computersMove) - 1]
    
    if usersMove[0] == computersMove[0]:
        ties += 1
        print(computersMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    elif usersMove[0] == lossingMove[0]:
        losses += 1
        print(lossingMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    elif usersMove[0] == winningMove[0]:
        wins += 1
        print(winningMove.upper(), "versus...")
        print(computersMove.upper())
        continue
    else:
        
        updateRpsData()
        print("Feel free to Continue when you return")
        print("Quiting...")
        sys.exit()
