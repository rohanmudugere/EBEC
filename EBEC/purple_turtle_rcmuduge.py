"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 05.4 - Purple Turtle
Date: 03/05/2022

Description:
    This program draws out the phrase purple turtle.

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
    setup(600, 400)
    width(9)
    color("purple")

def draw_e():
    start = position()
    goto(start[0] + 60, start[1] + 30) #move to start letter
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

def draw_l():
    start = position()
    pendown()
    setheading(90)
    forward(100) 
    penup()
    goto(start[0] + 30, start[1]) 

def draw_p():
    start = position()
    goto(start[0], start[1] + 60) 
    setheading(270)
    pendown()
    forward(100) 
    penup()
    setheading(90)
    forward(70)
    pendown()
    setheading(270)
    circle(30, 360) 
    penup()
    spot = position()
    goto(spot[0] + 90, spot[1] - 30) 


def draw_r():
    setheading(90)
    pendown()
    forward(60) 
    penup()
    setheading(270)
    forward(30)
    setheading(270)
    pendown()
    circle(30, -90) 
    spot = position()
    penup()
    goto(spot[0] + 30, spot[1] - 60) 

def draw_t():
    start = position()
    goto(start[0] + 30, start[1]) 
    pendown()
    setheading(90)
    forward(100) 
    setheading(270)
    forward(20)
    setheading(180)
    forward(25) 
    setheading(0)
    forward(50) 
    penup()
    goto(start[0] + 90, start[1]) 

def draw_u():
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
    spot = position()
    penup()
    goto(start[0] + 90, start[1]) 

def main():
    penup()
    goto(-200, 100) #starting point for word "purple"
    draw_p()
    draw_u()
    draw_r()
    draw_p()
    draw_l()
    draw_e()
    goto(-200, -100) 
    draw_t()
    draw_u()
    draw_r()
    draw_t()
    draw_l()
    draw_e()

if __name__ == '__main__':
    start()
    main()
    done()
