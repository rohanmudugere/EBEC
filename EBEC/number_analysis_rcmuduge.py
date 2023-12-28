"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 03/16/2022

Description:
    This program finds the maximum, minimum, sum, and average of a 10 number list. 

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
def get_number_list():
    list = []
    for i in range(1,11): #iterate 10 times
        num = float(input(f"  number {i:2d} of 10: "))
        list.append(num)
    return list

def main():
    print(f"Enter 10 numbers:")
    #user input and calculate values
    list = get_number_list()
    maximum = max(list)
    minimum = min(list)
    tot = sum(list)
    avg = tot / (len(list))
    #display results
    print(f"Highest number: {maximum:.2f}")
    print(f"Lowest number: {minimum:.2f}")
    print(f"Total: {tot:.2f}")
    print(f"Average: {avg:.2f}")

if __name__ == "__main__":
    main()
