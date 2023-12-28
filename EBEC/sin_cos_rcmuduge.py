"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 04/09/2022

Description:
    This program plots sin(x) and cos(x) in the interval [0, 2pi]. 

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
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots()
    #set axis limits
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 2 * np.pi)
    #set axis ticks
    ax.set_yticks([-1, 1])
    ax.set_xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    #generate x-values to use
    x = np.arange(0, 2 * np.pi, 0.1)
    #functions to plot
    y = np.sin(x)
    z = np.cos(x)
    #change spines
    for spine in ["right", "top"]:
        ax.spines[spine].set_visible(False)
    for spine in ["bottom", "left"]:
        ax.spines[spine].set_position("zero")
    #plot functions and add colors
    ax.plot(x, y, color = "r")
    ax.plot(x, z, color = "b")
    plt.show()

if __name__ == "__main__":
    main()
