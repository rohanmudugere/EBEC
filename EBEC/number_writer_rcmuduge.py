"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.4 - Number Writer
Date: 04/03/2022

Description:
    This program creates a file containing a specified number of integers in the range 1019 - 1215.

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
def randomNum():
    #generate and return number in the range 1019 - 1215
    from random import randrange as r
    num = r(1019, 1216) 
    return num

def main():
    numbers = int(input("How many numbers would you like? ")) #user input for numbers 
    with open("random_numbers.txt", "w") as file:
        #add specified amount of random numbers to file
        for i in range(numbers):
            num = str(randomNum())
            file.write(num + "\n")

if __name__ == "__main__":
    main()
