"""
Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h
"""
input_string = input("Please type in a string: ")
string_len = len(input_string)
n_letter = string_len -1
while n_letter >= 0:
    print(input_string[n_letter])
    n_letter -= 1
