"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 03.2 - Sum Average
Date: 02/17/2022

Description:
    This program calculates the sum and average of user inputs. 

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
    num = float(input("Enter a non-negative number (negative to quit): "))      #first user input

    if num >= 0:        #if first number is not negative
        numSum = num        #initialize sum
        i = 1       #initialize  number of inputs

        while num >= 0:     #while input is positive
            num = float(input("Enter a non-negative number (negative to quit): ")) 
            if num >= 0:
                i += 1      #update number of inputs
                numSum += num       #update sum
            else:       #if negative number is entered do not update sum or number of inputs
                i = i
                numSum = numSum
            
        avg = numSum / i    #calculate average

        #display results
        print(f"  You entered {i} numbers.")
        print(f"  Their sum is {numSum:.3f} and their average is {avg:.3f}.")
    else:       #if first input is negative this is the result
        print(f"  You didn't enter any numbers.")

if __name__ == "__main__":
    main()
