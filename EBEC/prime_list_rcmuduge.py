"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 04.5 - Prime List
Date: 02/26/2022

Description:
    This program lists all the prime numbers less than the number provided by the user. 

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
def is_prime(number):
    if number == 1: #if 1 is entered return false
        return False
    else:
        for n in range (2, int(number ** (1/2)) + 1): #iterate from 2 to squqre root of the number plus 1
            if (number % n) == 0: #check if number is divisible
                return False
        else: #if number is not divisible by any of these values it is prime 
            return True

def main():
    number = int(input("Enter a positive integer: "))
    print(f"The primes up to {number} are: ", end='')
    for n in range (1, number + 1):
        result = is_prime(n)
        if n == 2:
            print(f"2", end='')
        elif result == True:
            print(f", {n}", end='')

if __name__ == "__main__":
    main()
