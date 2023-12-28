"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 03/13/2022

Description:
    This program gives the user an addition question with a random two and three digit integer. 

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
def random_number(x):
    from random import randrange as r #import randrange from random module
    randNum = r(10 ** (x-1), 10 ** x) #random x-digit number
    return randNum

def main():
    num1 = random_number(2) #random two-digit number
    num2 = random_number(3) #random three-digit number

    print(f"   {num1:d}")
    print(f"+ {num2:d}")
    print(f"-----")
    answer = int(input("= "))
    
    if answer == (num1 + num2):
        print(f"Correct -- Good Work!") #display this if answer is correct
    else:
        print(f"Incorrect. The correct answer is {(num1 + num2):d}.") #display this if answer is incorrect

if __name__ == "__main__":
    main()
