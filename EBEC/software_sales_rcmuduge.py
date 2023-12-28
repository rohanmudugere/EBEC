"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/10/2022

Description:
    This program calculates the discount applied and total cost of purcahasing x packages. 

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
    """Write your mainline logic below this line (then delete this line)."""
    numPack = int(input("How many packages will be purchased: ")) 
    if numPack <= 0: #0 or less is an invalid input
        print(f"  Invalid Input!")
    elif (numPack >= 1) & (numPack <= 3): #range for discount
        print(f"  No discount applied.") #discount amount
        print(f"  The total price to purchase {numPack:d} packages is ${(numPack * 880):,.2f}.") #price of purchase
    elif (numPack >= 4) & (numPack <= 39): 
        print(f"  10% discount applied.")
        print(f"  The total price to purchase {numPack:d} packages is ${(numPack * 880 * 0.9):,.2f}.") 
    elif (numPack >= 40) & (numPack <= 199): 
        print(f"  15% discount applied.")
        print(f"  The total price to purchase {numPack:d} packages is ${(numPack * 880 * 0.85):,.2f}.") 
    elif (numPack >= 200) & (numPack <= 999): 
        print(f"  30% discount applied.")
        print(f"  The total price to purchase {numPack:d} packages is ${(numPack * 880 * 0.7):,.2f}.") 
    elif (numPack >= 1000): 
        print(f"  42% discount applied.")
        print(f"  The total price to purchase {numPack:d} packages is ${(numPack * 880 * 0.58):,.2f}.")
    
if __name__ == "__main__":
    main()
