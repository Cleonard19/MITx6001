"""
File Name: vowel_counter.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program counts the number of vowels in a string AND tells you how many times the word "bob" appears in the string


Purpose: Part of the EDx.org MIT6001 Course
"""

test_String = "dsfjsdhfikjdshbobfiudsbobyuweuroiweuriowbobeujiolxduviodsufiosbob"

word = input('Please enter a random string. I will determine the number of vowels and the number of Bob\'s: ')
vowel_count = 0
bob_count = 0

for index in range(len(word)):
    if word[index:index+3] == "bob":
        bob_count +=1
    if word[index] == "a" or word[index] == "e" or word[index]== "i" or word[index] == "o" or word[index] == "u":
        vowel_count += 1

print("Number of vowels: ", vowel_count)
print("number of bobs: ", bob_count)

# end