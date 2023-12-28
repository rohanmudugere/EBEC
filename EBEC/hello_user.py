"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 00.1 - Hello user
Date: 01/20/2022

Description:
    This program says hello to the user followed by their name.

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
    #User-input name
    name = input("What is your name? ") 
    #Display name with hello
    print(f"Hello {name}!") 
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
