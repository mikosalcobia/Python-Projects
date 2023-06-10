import random

x = int(input("Choose a number: "))
y = int(input("Choose another number: "))

print("\nThe range is from", x, "to", y,".\n")

n_PC = random.randint(x,y)
n_user = None

def higherOrlower(n_user):
    """Higher or lower number.

    Check if the user's number is higher or lower than the PC's.

    Args:
        n_user (int): User's number

    """
    if n_user < n_PC:
        print("It is a higher number\n")
    else:
        print("It is a lower number\n")


while n_user != n_PC:
    n_user = int(input("What's the number? "))

    if n_PC == n_user:
        print("Right, you won!")
    else:
        print("Try again")
        higherOrlower(n_user)
