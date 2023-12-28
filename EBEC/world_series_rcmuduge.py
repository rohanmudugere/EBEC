"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 09.2 - World Series 
Date: 04/07/2022

Description:
    This program returns the World Series winner for any gven year, as well as the number of times that team has won the World Series.  

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
def load_winners_data():
    with open("WorldSeriesWinners.txt") as file:
        #create list of winner for each year
        winnersList = file.readlines()
        for i in range(len(winnersList)):
            winnersList[i] = winnersList[i].strip()
        #create list of years excluding 1904, 1994
        years = []
        for i in range(1903, 2022):
            years.append(i)
        years.remove(1904)
        years.remove(1994)
        #create dictionary with year as key, winner as value
        winDict = {} 
        for i in range(len(years)):
            winDict[years[i]] = winnersList[i]
        numWins = {}
        for i in range(len(winnersList)):
            if winnersList[i] not in numWins:
                numWins[winnersList[i]] = 1
            else:
                numWins[winnersList[i]] += 1
        return numWins, winDict

def main():
    wins, winners = load_winners_data()
    #obtain and validate input year
    year = int(input("Enter a year in the range 1903 -- 2021: "))
    #display results
    if ((year < 1903) | (year > 2021)):
        print(f"  Data for the year {year} is not included in this system.")
    elif ((year == 1904) | (year == 1994)):
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        print(f"  The {winners[year]} won the World Series in {year}.")
        print(f"  They have won the World Series {wins[winners[year]]} times.")

if __name__ == "__main__":
    main()
