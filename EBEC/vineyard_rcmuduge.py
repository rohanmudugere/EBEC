"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 01.1 - Vineyard
Date: 02/02/2022

Description:
    Given the width of the end-post assembly, requried space between vines, and length of the row, this program calculates the number of grapevines that can fit in the row. 

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
    print(f"Enter each of the following quantities in meters.") #user directions
    width = float(input("  How wide is the end-post assembly? ")) #user input for width of end-post assembly
    space = float(input("  How much space should be between the vines? ")) #user input for space between vines
    length = float(input("  How long is this row? ")) #user input for row length
    numVines = (length - 2 * width)/space #calculate number of vines
    numVines = int(numVines) #round number of vines to smallest whole intger
    print(f"\nThere is enough space for {numVines} vine(s) in this row.") #print number of vines

if __name__ == "__main__":
    main()
