"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 03.4 - Organisms
Date: 02/18/2022

Description:
    This program predicts the size of a population given the starting population, average daily increase, and number of days to multiply. 

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
    population = float(input("Starting population, in thousands: "))
    growth = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))
    print(f"Day", end = "")
    print(f"   Approx. Pop")
    for x in range(days + 1): #iterate for number of days
        print(f"{x:3,.0f}", end = "")
        print(f"{(population * (1 + growth / 100) ** x):14,.3f}") #calculate and display predicted population

if __name__ == "__main__":
    main()
