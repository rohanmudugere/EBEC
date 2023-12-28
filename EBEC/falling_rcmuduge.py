"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 04.1 - Falling
Date: 02/26/2022

Description:
    This program calculates the distance an object has fallen from 5 to 50 seconds (in increments of 5 seconds). 

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
def falling_dist(time):
    g = 8.87 #define gravitational constant
    dist = 1/2 * g * time ** 2
    return dist

def main():
    print(f"Time (s)  Distance (m)\n----------------------")
    for time in range (5, 55, 5): #use multiples of 5 between 5 and 50
        dist = falling_dist(time)
        print(f"{time:8d}{dist:14.1f}")

if __name__ == "__main__":
    main()
