"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 04/07/2022

Description:
    This program quizzes the user on their knowledge of state capitals. 

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
import random as r
from tempfile import tempdir

def get_state_data():
    with open("EBEC/state_capitals.txt") as file:
        #add states and corresponding capitals to one list
        statesList = file.readlines()
        for i in range(len(statesList)):
           statesList[i] = statesList[i].strip()
        statesAndCaps = []
        for line in statesList:
            line = line.split(", ")
            statesAndCaps.extend(line)
        #create dictionary using capitals as the key
        answerKey = {}
        for i in range(0, len(statesAndCaps) - 1, 2):
            answerKey[statesAndCaps[i]] = statesAndCaps[i+1]
        #swap keys and values so that state name is the key
        answerKey = dict([(value, key) for key, value in answerKey.items()])
        return answerKey

def main():
    #initialize variables
    answerKey = get_state_data()
    states = list(answerKey.keys())
    numCorrect = 0
    numAttempts = 0
    userAns = str()
    while userAns != str(0):
        #randomly select a state and prompt user to enter its capital
        state = r.choice(states)
        userAns = input(f"What is the capital of {state} (enter 0 to quit)? ")
        userAns = userAns.title()
        numAttempts += 1
        if userAns == answerKey[state]:
            numCorrect += 1
            print(f"  That is correct!")
        elif userAns == str(0):
            print(f"You answered {numCorrect} out of {numAttempts - 1} questions correctly.")
        else:
            print(f"  That is incorrect.")

if __name__ == "__main__":
    main()
