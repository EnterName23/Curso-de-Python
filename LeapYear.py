"""
Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.
"""



year = int(input("Please type in a year"))

div_by_4 = (year % 4 == 0)
div_by_100 = (year % 100 == 0)
div_by_400 = (year % 400 == 0)

verif_leap_year = (div_by_4 and not div_by_100) or div_by_400


if verif_leap_year:
    print("That year is a leap year")

else:
    print("That year is not a leap year")
