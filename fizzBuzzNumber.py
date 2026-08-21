nbr = int(input("Enter an Integer "))
if nbr % 3 == 0 and nbr % 5 == 0:
    print("Fizz Buzz")
elif nbr % 3 == 0:
    print("Fizz")
elif nbr % 5 == 0:
    print("Buzz")
else:
    print(nbr)