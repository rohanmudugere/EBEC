"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 02/10/2022

Description:
    This program determines the color of a given pocket.

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
    pocketNum = int(input("Please choose a pocket number: ")) #user input for pocket number
    #selection structure
    if (pocketNum < 0) | (pocketNum > 36): 
        print(f"  Invalid Input!")
    elif pocketNum == 0:
        print(f"  Pocket number {pocketNum:d} is green.")
    elif (pocketNum >= 1) & (pocketNum <= 10) & (pocketNum % 2 != 0): 
        print(f"  Pocket number {pocketNum:d} is red.")
    elif (pocketNum >= 1) & (pocketNum <= 10) & (pocketNum % 2 == 0): 
        print(f"  Pocket number {pocketNum:d} is black.")
    elif (pocketNum >= 11) & (pocketNum <= 18) & (pocketNum % 2 != 0): 
        print(f"  Pocket number {pocketNum:d} is black.")
    elif (pocketNum >= 11) & (pocketNum <= 18) & (pocketNum % 2 == 0): 
        print(f"  Pocket number {pocketNum:d} is red.")
    elif (pocketNum >= 19) & (pocketNum <= 28) & (pocketNum % 2 != 0): 
        print(f"  Pocket number {pocketNum:d} is red.")
    elif (pocketNum >=19) & (pocketNum <= 28) & (pocketNum % 2 == 0): 
        print(f"  Pocket number {pocketNum:d} is black.")
    elif (pocketNum >= 29) & (pocketNum <= 36) & (pocketNum % 2 != 0): 
        print(f"  Pocket number {pocketNum:d} is black.")
    elif (pocketNum >= 29) & (pocketNum <= 36) & (pocketNum % 2 == 0): 
        print(f"  Pocket number {pocketNum:d} is red.")

if __name__ == "__main__":
    main()
