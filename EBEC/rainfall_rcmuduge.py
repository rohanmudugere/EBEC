"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 03.3 - Rainfall
Date: 02/18/2022

Description:
    This program calculates the total and average rainfall over a period of time measured in years. 

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
    month = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."] 
    rfStr = str("Enter the rainfall for") 
    invInputStr = str("Invalid input; rainfall cannot be negative.")
    totRainFall = 0
    
    numYrs = int(input("Enter the number of years: ")) #user input for number of years
    if numYrs <= 0: #if number of years is 0 or less input is invalid
        print(f"Invalid input; years must be greater than 0.")
    else: 
        for x in range(numYrs): #indexing with number of years
            print(f"  For year No. {x+1}")
            for y in range(len(month)): #indexing using the number of months
                rfAmt = float(input(f"    {rfStr} {month[y]}: "))
                while rfAmt < 0: #prompt user to re-enter if negative rainfall is initially entered
                    print(f"    {invInputStr}")
                    rfAmt = float(input(f"    {rfStr} {month[y]}: "))
                totRainFall += rfAmt #update total rainfall
            avgRainFall = totRainFall / (numYrs * 12)         
            #display outputs
        print(f"There are {numYrs * 12} months.")
        print(f"The total rainfall was {totRainFall:.2f} inches.")
        print(f"The monthly average rainfall was {avgRainFall:.2f} inches.")

if __name__ == "__main__":
    main()
