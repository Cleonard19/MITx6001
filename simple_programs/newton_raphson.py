"""
File Name: newton_raphson.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program approximates the square root of numbers using the newton-raphson principle

Purpose: Part of the EDx.org MIT6001 Course
"""
y = float(input("What number would you like to find the square root of? "))

epsilon = float(input("How close would you like your approximation of %f to be? " % y))

guess = y/2.0

num_guesses = 0

while abs(guess*guess - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))

print("Number of Guesses = " + str(num_guesses))
print("The square root of %f is about %f" % (y, guess) )

# end
