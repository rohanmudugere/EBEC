"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.6 - Step Counter
Date: 03/39/2022

Description:
    This program finds the number of steps taken each month. 

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
    with open("steps.txt") as file:
        steps = file.readlines()
        #initialize totala number of steps for each month
        janSteps = 0
        febSteps = 0
        marSteps = 0
        aprSteps = 0
        maySteps = 0
        junSteps = 0
        julSteps = 0
        augSteps = 0
        septSteps = 0
        octSteps = 0
        novSteps = 0
        decSteps = 0
        #convert all list element to int data type
        for i in range(len(steps)):
            steps[i] = int(steps[i])
        #calculate total number of steps for each month
        for i in range(365):
            if i < 31:
                janSteps += steps[i]
            elif i < 59:
                febSteps += steps[i]
            elif i < 90:
                marSteps += steps[i]
            elif i < 120:
                aprSteps += steps[i]
            elif i < 151:
                maySteps += steps[i]
            elif i < 181:
                junSteps += steps[i]
            elif i < 212:
                julSteps += steps[i]
            elif i < 243:
                augSteps += steps[i]
            elif i < 273:
                septSteps += steps[i]
            elif i < 304:
                octSteps += steps[i]
            elif i < 334:
                novSteps += steps[i]
            elif i < 365:
                decSteps += steps[i]
    #display avrage daily steps for each month
    print(f"The average steps taken each month were:")
    print(f"   January : {(janSteps/31):.2f}")
    print(f"  February : {(febSteps/28):.2f}")
    print(f"     March : {(marSteps/31):.2f}")
    print(f"     April : {(aprSteps/30):.2f}")
    print(f"       May : {(maySteps/31):.2f}")
    print(f"      June : {(junSteps/30):.2f}")
    print(f"      July : {(julSteps/31):.2f}")
    print(f"    August : {(augSteps/31):.2f}")
    print(f" September : {(septSteps/30):.2f}")
    print(f"   October : {(octSteps/31):.2f}")
    print(f"  November : {(novSteps/30):.2f}")
    print(f"  December : {(decSteps/31):.2f}")

if __name__ == "__main__":
    main()
