"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.5 - Number Reader
Date: 03/39/2022

Description:
    This program reads a file, then calculates and displays statistics about it. 

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
    numSum = 0
    with open("random_numbers.txt") as file:
        numbers = file.readlines()
        numLines = len(numbers) #find number of elements
        for i in range(numLines):
            numbers[i] = int(numbers[i])
        minimum = min(numbers)
        maximum = max(numbers)
        for i in range(numLines):
            numSum += int(numbers[i]) #calculate sum of numbers
    avg = numSum / numLines 
    #display outputs
    print(f"{numLines:,d} numbers were read from the file.")
    print(f"Min: {minimum:,d}")
    print(f"Max: {maximum:,d}")
    print(f"Sum: {numSum:,d}")
    print(f"Avg: {avg:,.1f}")

if __name__ == "__main__":
    main()
