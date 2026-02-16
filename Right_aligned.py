"""
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python

**************python
Sample output
Please type in a string: alongerstring

*******alongerstring
Sample output
Please type in a string: averyverylongstring

*averyverylongstring
"""
while True:
    input_string = input("Please type in a string: ")
    string_len = len(input_string)
    if string_len > 20:
        print("This string is too long")
        continue
    star_len = 20 - string_len
    print ("*"*star_len + input_string)
    break

