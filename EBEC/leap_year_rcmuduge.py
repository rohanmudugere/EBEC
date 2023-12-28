"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 02.1 - Leap Year
Date: 02/10/2022

Description:
    This program determines whether a year is a leap year or not.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

def main():
    year = int(input("Enter a year: "))
    if (year % 100 == 0) & (year % 400 != 0): #not a leap year if the year is not divisible by 400
        print(f"The year {year:d} is not a leap year.")
        print(f"February of {year:d} has 28 days.")
    elif (year % 4 == 0): #is a leap year if the year is divisible by 4 
        print(f"The year {year:d} is a leap year.")
        print(f"February of {year:d} has 29 days.")
    else: #if not divisible by 400 or 4 the year is not a leap year
        print(f"The year {year:d} is not leap year.")
        print(f"February of {year:d} has 28 days.")
        
if __name__ == "__main__":
    main()
