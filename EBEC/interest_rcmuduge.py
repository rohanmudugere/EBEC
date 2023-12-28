"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 01.2 - Interest
Date: 02/02/2022

Description:
    Given the inital deposiit, interset rate, years the account has earned interest, and the number of times 
    interest is compounded each year, this program will calculate the account balance. 

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
    print(f"Enter the following parameters.")
    initialDep = int(input("  The initial deposit? ")) #user input for initial deposit
    intRate = float(input("  The annual interest rate in percent? ")) #user input for interest rate
    intPercent = intRate/100 #convert interest rate to correct demical place
    years = float(input("  The number of years the account earn interest? ")) #user input for years that account has earned interest
    timesComp = int(input("  The number of times interest is compounded each year: ")) #user inputf for times compounded each year
    futureVal = initialDep * (1 + intPercent/timesComp) ** (timesComp * years) #calculate account balance
    print(f"The balance of this account will be ${futureVal:,.2f} after {years:.1f} years.") #display account balance

if __name__ == "__main__":
    main()
