"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 04/09/2022

Description:
    This program creates a pie chart for monthly sales. 

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
    #create list of months, get input for sales for each month
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthlySales = []
    #repeat input for each month
    for i in range(len(months)):
        sales = input(f"Enter the sales for {months[i]}: ")
        monthlySales.append(sales)

    #create pie chart with appropriate sales values, colors, and labels
    fig, ax = plt.subplots()
    y = monthlySales
    #provided colors
    c = ("#4D4038", "#BAA892", "#5B6870", "#6E99B4", "#A3D6D7", "#085C11", "#849E2A", "#C3BE0B", "#E9E45B", "#6B4536", "#B46012", "#FF9B1A")
    l = months
    ax.pie(y, colors = c, labels = l)
    #figure title
    ax.set_title("Monthly Sales Values")
    plt.show()

if __name__ == "__main__":
    main()
