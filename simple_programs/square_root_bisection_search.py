"""
File Name: square_root_bisection_search.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program will find a number near the perfect square root for a given input.

Purpose: Part of the EDx.org MIT6001 Course
"""


x = int(input("What number would you like to find the square root of? "))
epsilon = float(input("How close would you like to get to the perfect answer (epsilon)? "))
num_guesses = 0
low = 0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print ("Low = " + str(low) + " High = " + str(high) + " Answer = " + str(ans))
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) /2.0

print("Number of Guesses = " + str(num_guesses))
print(str(ans), "is close enough to the square root of", str(x))

# end
