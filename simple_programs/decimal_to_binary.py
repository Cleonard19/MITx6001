"""
File Name: decimal_to_binary.py
Created On: Fri Mar 1 2019
Author: Chris Leonard
Description: This program converts decimal numbers to binary numbers to reflect how the computer achieves this

Purpose: Part of the EDx.org MIT6001 Course
"""


flag = input("Is your number a floating point number, or an integer? ('i' for int 'f' for decimal) ")
result =''
p=0

if flag == 'i':
    num = int(input("Please enter your integer: "))
    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False

    if num == 0:
        result = '0'

    while num > 0:
        # returns modulus, adds it to the existing result
        result = str(num % 2) + result
        # returns integer quotient (floor division)
        num = num // 2
    if is_neg is True:
        result = "-" + result
elif flag == 'f':
    x = float(input("Please enter your decimal number between 0 and 1: "))
    while ((2**p) * x)%1 != 0:
        print("Remainder = " + str((2**p)*x - int((2**p)*x)))
        p += 1

    num = int(x*(2**p))

    if num == 0:
        result = '0'

    while num > 0:
        # returns modulus, adds it to the existing result
        result = str(num % 2) + result
        # returns integer quotient (floor division)
        num = num // 2

    for i in range(p-len(result)):
        result = "0" + result
    result = result[0:-p] + "." + result[-p:]

print("Your result is: ", result)

# end
