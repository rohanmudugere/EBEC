"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 03/16/2022

Description:
    This program calculates the frequency of each result when rolling two 6-sided die one million times. 

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
def roll_d6():
    import random as r
    roll = r.randrange(1,7) #generate random number between 1 and 6 inclusive of both
    return roll

def get_2d6_rolls(x):
    results = []
    for i in range(x): #iterate for number of rolls
        roll = roll_d6() + roll_d6()
        results.append(roll) #add roll to results array
    return results

def main():
    numRolls = 1000000
    results = get_2d6_rolls(numRolls)
    print(f"Roll  Frequency")
    for i in range(2, 13): #iterate for possible roll values
        freq = results.count(i)/numRolls * 100
        print(f" {i:2d}    {freq:5.2f}%")

if __name__ == "__main__":
    main()
