# Method to generate random integers
from random import randint

# Check if the user's response is an integer
from test_input import int_input

# Useful methods
from util import clear

# Clean the console
clear()
# Random number between 1 and 100
rn = randint(1, 100)

answer = int_input("Enter integer between 1 - 100: ")

attempts = 0
# As long as the answer is wrong, ask again
while answer != rn:
    attempts += 1
    answer = int_input("Wrong answer, try again: ", True)
    if answer > rn:
        print("The number is less")
    elif answer < rn:
        print("The number is higher")
    else:
        # Variable interpolation
        clear()
        print(f"Correct answer, you made it in {attempts} attempts.")