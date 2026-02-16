"""
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long
"""

string1 = input("Please type in a string 1:")
string2 = input("Please type in a string 2:")
string1_len = len(string1)
string2_len = len(string2)

if string1_len > string2_len:
    print(f"{string1} is longer")
elif string2_len > string1_len:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")
