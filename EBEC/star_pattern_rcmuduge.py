"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 03/03/2022

Description:
    This program draws a star with a specified number of points. 

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    numPoints = int(input("How many points do you want the star to have? "))
    innerAng = 360 / numPoints
    outerAng = 2 * innerAng
    right((180 - outerAng) / 2) #turn to draw first side
    color("black", "pink")
    begin_fill()
    for i in range (numPoints): #iterate for number of points
        forward(60) #move start current side
        left(180 - innerAng) #turn to complete current side
        forward(60) #move to complete current side
        right(180 - outerAng) #turn to draw second next
    end_fill()
        
if __name__ == '__main__':
    start()
    main()
    done()
