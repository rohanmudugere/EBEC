"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 07.4 - Magic Square
Date: 03/16/2022

Description:
    This program determines if 3 lists create a Lo Shu magic square.

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
def print_square(x):
    print(f"  {x[0][0]} {x[0][1]} {x[0][2]}") #display row one
    print(f"  {x[1][0]} {x[1][1]} {x[1][2]}") #dislay row two
    print(f"  {x[2][0]} {x[2][1]} {x[2][2]}") #display row three

def is_magic(x):
    if ((x[0][0] == 5) & (x[0][1] == 5) & (x[0][2] == 5)):
        return bool(False) #if a number is present more than once return false
    elif ((x[0][0] + x[0][1] + x[0][2]) == 15) & ((x[1][0] + x[1][1] + x[1][2]) == 15) & ((x[2][0] + x[2][1] + x[2][2]) == 15) & ((x[0][0] + x[1][0] + x[2][0]) == 15) & ((x[0][1] + x[1][1] + x[2][1]) == 15) & ((x[0][2] + x[1][2] + x[2][2]) == 15) & ((x[0][0] + x[1][1] + x[2][2]) == 15) & ((x[0][2] + x[1][1] + x[2][0]) == 15):
        return bool(True) #if these sums are equal to 15 return true
    else:
        return bool(False) #return false for all other conditions

def main():
    #initialize the lists
    one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    two = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    three = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    #get results for each list
    for i in [one, two, three]: #iterate for each list
        print(f"Your square is:")
        print_square(i)
        result = is_magic(i)
        if result == True:
            print(f"It is a Lo Shu magic square!\n") #result if true
        else: 
            print(f"It is not a Lo Shu magic square.\n") #result if false

if __name__ == "__main__":
    main()
