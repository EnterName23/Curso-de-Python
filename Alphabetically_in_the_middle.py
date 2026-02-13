"""
Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.
"""

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter2 <= letter1 <= letter3 or letter3 <= letter1 <= letter2:
    middle_letter = letter1
elif letter1 <= letter2 <= letter3 or letter3 <= letter2 <= letter1:
    middle_letter = letter2
else:
    middle_letter = letter3

print(f"The letter in the middle is {middle_letter}")
