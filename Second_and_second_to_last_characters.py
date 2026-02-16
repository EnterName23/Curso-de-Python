"""
Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""
input_string = input("Please type in a string: ")
index = len(input_string) - 1

if index > 1:
    second_last = input_string[index - 1] # second last character
    second = input_string[1] # second character
    if second == second_last:
        print(f"The second and the second to last characters are {second}")
    else:
        print("The second and the second to last characters are different")
else:
    print("There's no second or last second character.")
