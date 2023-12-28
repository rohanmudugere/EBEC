"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/14/2022

Description:
    This program contains the function to draw each vowel

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

def draw_a():
    #draw letter a
    """Complete this function to draw the character a."""
    start = position()
    setheading(0)
    goto(start[0] + 30, start[1])
    pendown()
    circle(30)
    penup()
    forward(30)
    pendown()
    setheading(90)
    forward(60)
    penup()
    spot = position()
    goto(spot[0] + 30, spot[1] - 60)

def draw_e():
    #draw letter e
    """Complete this function to draw the character e."""
    start = position()
    goto(start[0] + 60, start[1] + 30)
    pendown()
    setheading(90)
    circle(30, 300) 
    penup()
    goto(start[0] + 60, start[1] + 30)
    pendown()
    setheading(180)
    forward(60) 
    penup()
    spot = position()
    goto(spot[0] + 90, spot[1] - 30) 

def draw_i():
    #draw letter i
    """Complete this function to draw the character i."""
    start = position()
    pendown()
    setheading(90)
    forward(60)
    penup()
    forward(20)
    setheading(0)
    pendown()
    circle(4)
    penup()
    goto(start[0] + 30, start[1])

def draw_o():
    #draw letter o
    """Complete this function to draw the character o."""
    start = position()
    goto(start[0] + 60, start[1] + 30)
    pendown()
    circle(30)
    penup()
    goto(start[0] + 90, start[1])

def draw_u():
    #draw letter u
    """Complete this function to draw the character u."""
    start = position()
    goto(start[0], start[1] + 30) 
    pendown()
    setheading(270)
    circle(30, 180) 
    forward(30) 
    setheading(270)
    forward(60) 
    penup()
    goto(start[0], start[1] + 30)
    pendown()
    setheading(90)
    forward(30) 
    penup()
    goto(start[0] + 90, start[1])

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
