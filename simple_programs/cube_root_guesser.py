"""
File Name: cube_root_guesser.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program will brute force guess/check for the cube root of an input

Purpose: Part of the EDx.org MIT6001 Course
"""

cube = int(input("Enter a Cube: "))
epsilon = float(input("How close would you like to get to the perfect cube (epsilon)? "))

guess = 0.0
increment = .0001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("Number of Guesses = ", num_guesses)

if abs(guess ** 3 - cube) >= epsilon:
    print("Failed on cubed root of", cube)
else:
    print(guess, "is close enough tot he cube root of", cube)

# end
