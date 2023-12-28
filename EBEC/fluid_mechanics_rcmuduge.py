"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 02/12/2022

Description:
    This program calculates the Reynolds number for flow given temperature, velocity, and diameter. 

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
    #user inputs
    temp = float(input("Enter the temperature in °C as 5, 20, or 50: "))
    vel = float(input("Enter the velocity of water in the pipe (m/s): "))
    diameter = float(input("Enter the pipe's diameter (m): "))
    
    #kinematic viscosity at given temperature
    if temp == 5:
        kinVis = 1.52 * 10 ** (-6)
    elif temp == 20:
        kinVis = 1.00 * 10 ** (-6)
    else: 
        kinVis = 5.54 * 10 ** (-7)

    re = (vel * diameter) / kinVis #calculate Reynolds number

    #display results
    print(f"At {temp}°C, the Reynolds number for flow at {vel} m/s in a {diameter} m diameter pipe is {re:.2e}.")

if __name__ == "__main__":
    main()
