"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 03/29/2022

Description:
    This program converts a string to pig latin. 

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
def pig(sentance):
    words = sentance.split()
    ending = str("ay") 
    pigLatin = []
    for word in words:
        pigLatin.append(word[1:] + word[0] + ending) #convert each word to pig latin
    addSpace = " ".join(pigLatin) 
    addCap = addSpace.capitalize()
    return addCap 

def main():
    sentance = str(input("Enter a string: ")) #get user input
    pigLatin = pig(sentance)
    print(f"Pig latin: {pigLatin}") #display pig latin sentance 

if __name__ == "__main__":
    main()
