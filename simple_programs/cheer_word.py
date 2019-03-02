"""
File Name: cheer_word.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program will be your personal cheerleader for any word you enter


Purpose: Part of the EDx.org MIT6001 Course
"""

# This string holds all the letters that should be prefaced by "an" instead of "a"
an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "!   " + char)
    else:
        print("Give me a " + char + "!   " + char)
    i += 1

print("What does that spell!?")
for i in range(times):
    print(word, "!!!")

# end
