import math


"""
12. Medium
     Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it 
making four. The same principle applies to the number nine, which is written as IX. There are six instances 
where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
"""


def intToRoman(num):

    num_extract = {}
    values = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    for letter, val in values.items():
        quotient = math.floor(num/val)
        num_extract[letter] = quotient
        num -= quotient * val

    roman_num = ""
    for letter, val in num_extract.items():
        if (letter == "M" and val == 1 and num_extract["C"] == 4):
            roman_num += "CM"

        elif (letter == "C" and val == 4):  # 100
            if (num_extract["D"] == 0):
                roman_num += "CD"

        elif (letter == "L" and val == 1 and num_extract["X"] == 4):  # 50
            roman_num += "XC"

        elif (letter == "X" and val == 4):  # 10
            if (num_extract["L"] == 0):
                roman_num += "XL"

        elif (letter == "V" and val == 1 and num_extract["I"] == 4):
            roman_num += "IX"

        elif (letter == "I" and val == 4):
            if (num_extract["V"] == 0):
                roman_num += "IV"

        else:
            roman_num += add_roman_number(letter, val)

    return roman_num


def add_roman_number(letter, repetitions):
    roman_number = ""
    for i in range(repetitions):
        roman_number += letter
    return roman_number


num = 3
numero = intToRoman(num)
print("=======================================================")
print(f"Number {num} in roman is like {numero}")
print("=======================================================")
