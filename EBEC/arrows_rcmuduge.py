"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 03.1 - Arrows
Date: 02/18/2022

Description:
    This program displays the number of arrows that a user inputs. 

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
    numArrows = int(input("Enter the number of arrows to draw: "))  #user input for number of arrows
    for i in range(0, numArrows): #iterate for number of arrows
        print(f"<", end = "")
        for n in range(0, i): #iterate for number of equals signs
            print(f"=", end = "")
        print(">")
    
if __name__ == "__main__":
    main()
