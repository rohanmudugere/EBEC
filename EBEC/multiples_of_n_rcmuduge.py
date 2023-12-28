"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 03/16/2022

Description:
    This program displays all values in a list that are multiples of a number. 

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
def multiples_of(x, y):
    list = []
    for i in range(len(y)): #iterate for number of values in list
        if ((y[i] % x) == 0):
            list.append(y[i]) #add multiple to new list
    return(list)

def main():
    ogList = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    num = 13
    multiples = multiples_of(num, ogList)
    #display results
    print(f"Original list of numbers:")
    print(f"  {ogList}")
    print(f"Numbers in the list that are multiples of 13:")
    print(f"  {multiples}")

if __name__ == "__main__":
    main()
