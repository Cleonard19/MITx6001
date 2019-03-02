"""
File Name: number_guesser.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program will guess your number (between 0 and 100 [non-inclusive])

Purpose: Part of the EDx.org MIT6001 Course
"""

print("Please think of an integer between 0 and 100!")

high = 100
low = 0
toggle = ""

while toggle != "c":
    guess = (high + low) // 2
    print("Is your secret number", guess, "?")
    toggle = input("Enter 'h' to indicate the guess is too high. Enter 'l' "
                   "to indicate the guess is too low. Enter 'c' to indicate that I have guessed correctly")
    if toggle == 'h':
        high = guess
        toggle = ''
    elif toggle == 'l':
        low = guess
        toggle = ''
    elif toggle == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secrent number was:", guess)

# end
