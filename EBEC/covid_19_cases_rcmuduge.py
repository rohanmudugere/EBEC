"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 04/09/2022

Description:
    This program plots the daily positive COVID-19 cases in Indiana. 

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
import datetime

def main():
    with open("EBEC/indiana_covid-19_data_spring_2022.txt") as file:
        #store all words in list
        data = []
        dailyData = file.readlines()
        for line in dailyData:
            data.extend(line.split())
        #extract only dates and positive cases with indexing
        dates = []
        positiveCases = []
        newCases = 0
        totCases = []
        for i in range(len(data)):
            data[i] = data[i].strip()
            if i % 4 == 0:
                dates.append(data[i])
            elif i % 4 == 2:
                positiveCases.append(data[i])
                newCases += int(data[i]) / 1000
                totCases.append(newCases[i])
    #plot data
    fig, ax = plt.subplots()
    #convert date data so it is evenly spaced
    x = []
    for date in dates:
        y, m, d = date.split("-")
        dt = datetime.date(int(y), int(m), int(d))
        x.append(dt)
    y = totCases
    #plot labels
    ax.set_ylabel("Number of Cases (in thousands)")
    ax.set_xlabel("Date")
    ax.set_title("Positive COVID-19 Cases in Indiana")
    #plot formatting
    ax.bar(x,y, width=1)
    fig.autofmt_xdate()
    plt.show()

if __name__ == "__main__":
    main()
