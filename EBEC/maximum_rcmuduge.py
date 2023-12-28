"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 04.2 - Maximum
Date: 02/26/2022

Description:
    This program returns the larger value of user two inputs.

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
def max_of_two(n1, n2):
    #return first number if it is larger, or second number if it is smaller
    if n1 > n2: 
        return n1
    else: 
        return n2

def main():
    #user inputs
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))
    
    greaterNum = max_of_two(number1, number2)
    print(f"The number {greaterNum} is greater.") #display larger value
    
if __name__ == "__main__":
    main()
