"""
Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
The program should then print out the number of times the user tried different codes.

Sample output
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts

If the user gets it right on the first try, the program should print out something a bit different:

Sample output
PIN: 4321
Correct! It only took you one single attempt!
"""

pin_reg = 4321

attempts = 1
while True:
    pin_input = int(input("PIN:"))
    if pin_input == pin_reg:
        if attempts == 1:
            print(f"Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        print("Wrong")
    attempts += 1
