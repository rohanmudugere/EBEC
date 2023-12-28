"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/14/2022

Description:
    This program draws vowels in a random order.

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
import random as r
import vowels as v
from turtle import *

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
    """Write your mainline logic below this line (then delete this line)."""
    order = ["a", "e", "i", "o", "u"]
    r.shuffle(order) #scramble letters in list
    for x in range(0,5): #iterate for number of elements in list
        #draw letter based on what is in each position of list
        if order[x] == "a":
            v.draw_a()
        elif order[x] == "e":
            v.draw_e()
        elif order[x] == "i":
            v.draw_i()
        elif order[x] == "o":
            v.draw_o()
        else:
            v.draw_u()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
