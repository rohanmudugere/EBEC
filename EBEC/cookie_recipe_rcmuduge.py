"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/20/2022

Description:
    Given the user's deired amount of cookies, this program will calculate
    the amount of butter, sugar, and flour required to make this amount
    of cookies. 

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
    numCookies = int(input("How many cookies do you want to make? "))
    amountButter = float(1.25/48 * numCookies) #calculate amount of butter in cups
    amountSugar = float(1.5/48 * numCookies)   #calculate amount of sugar in cups
    amountFlour = float(2.5/48 * numCookies)   #calculate amount of sugar in cups
    print(f"To make {numCookies:,d} cookies, you will need:")   
    print(f"{amountButter:10,.2f} cups of butter")  #print amount of butter
    print(f"{amountSugar:10,.2f} cups of sugar")    #print amount of sugar
    print(f"{amountFlour:10,.2f} cups of flour")    #print amount of flour

if __name__ == "__main__":
    main()
