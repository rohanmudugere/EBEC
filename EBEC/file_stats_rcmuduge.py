"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.3 - File Stats
Date: 04/03/2022

Description:
    This program displays the statistics of a specific file. 

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
    numWords = 0
    numLines = 0
    with open("frontiero_v_richardson.txt") as file:
        for line in file:
            numWords += len(line.split()) #add number of words in each line
            numLines += 1 #count total number of lines
    #program outputs
    print(f"Total number of words: {numWords}")
    print(f"Total number of lines: {numLines}")
    print(f"Average number of words per line: {(numWords/numLines):.1f}")

if __name__ == "__main__":
    main()
