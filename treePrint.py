import random

treeHeight = int(input("Enter the tree size: "))

def treeWidth(height) ->int:
    return 1 + 2 * (height - 1)

maxTreeWidth = treeWidth(treeHeight)

for height in range(treeHeight):
    currentTreeWidth = treeWidth(height+1)
    spaces = " " * ((maxTreeWidth - currentTreeWidth)//2)
    branches = "^" * currentTreeWidth

    # Christmas Decorations
    chances = min(1, currentTreeWidth)
    while chances > 0:
        ballIndex = random.randrange(currentTreeWidth)
        if ballIndex < currentTreeWidth:
            branches = branches[:ballIndex] + "o" + branches[ballIndex+1:]
        chances -= 1

    print(spaces + branches)

trunk = " " * (maxTreeWidth // 2) + "#"
print(trunk + "\n" + trunk)