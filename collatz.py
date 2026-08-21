import sys

def collatz(nbr):
    if nbr == 1:
        return
    if nbr % 2 == 0:
        print(nbr // 2, end=" ")
        collatz(nbr // 2)
    else:
        print(3 * nbr + 1, end=" ")
        collatz(3 * nbr + 1)


try:
    nbr = int(input("Enter and integer: "))
except ValueError:
    print("Invalid Integer entered")
    sys.exit()

collatz(nbr)
print()
