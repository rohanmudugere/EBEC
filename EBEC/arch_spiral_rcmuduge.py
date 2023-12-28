"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 06.4 - Arch Spiral
Date: 03/14/2022

Description:
    This program draws the archimedean spiral.

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
import math as m

def start():
    setup(564, 564)
    width(5)

def main():
    for angleDeg in range(2161): #iterate for number of degrees in 6 circles
        angleRad = angleDeg * m.pi / 180 #convert from degrees to radians
        #equations for x and y coordinates
        x = angleDeg / (m.pi ** 2) * m.cos(angleRad) 
        y = angleDeg / (m.pi ** 2) * m.sin(angleRad)
        goto(x, y)

if __name__ == "__main__":
    start()
    main()
    done()
