"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 04/09/2022

Description:
    This program plots the average weekly price of gas in the year 2008. 

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

def main():
    #create list of average price for each week
    with open("2008_Weekly_Gas_Averages.txt") as file:
        prices = file.readlines()
        gasPrices = []
        for i in range(len(prices)):
            prices[i] = float(prices[i].strip())
            gasPrices.append(prices[i])
    #create list of weeks
    weeks = []
    for i in range(1, len(gasPrices) + 1):
        weeks.append(i)
    #plot data
    fig, ax = plt.subplots()
    #plotted variables
    x = weeks
    y = gasPrices
    #axis limits
    ax.set_ylim(1.5, 4.25)
    ax.set_xlim(1, len(weeks))
    #axis ticks
    ax.set_yticks([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    ax.set_xticks([10, 20, 30, 40, 50])
    #plot labels
    ax.set_ylabel("Average Price (dollars/gallon)")
    ax.set_xlabel("Weeks (by number)")
    ax.set_title("2008 Weekly Gas Prices")
    ax.grid()
    ax.plot(x,y)
    plt.show()

if __name__ == "__main__":
    main()
