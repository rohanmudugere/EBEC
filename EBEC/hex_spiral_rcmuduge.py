"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 05.2 - Hex Spiral
Date: 03/03/2022

Description:
    This program draws a hexagonal spiral. 

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
from turtle import *

def start():
    setup(564, 564)
    width('5')

def main():
    i = 0 #index for loop
    for i in range (39): #iterate to number of sides
        i += 1
        forward(i * 6) #increase length by 6
        right(60) #turn 60 degrees

if __name__ == "__main__":
    start()
    main()
    done()
