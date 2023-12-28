"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 03/13/2022

Description:
    This program simulates a game of rock paper scissors. 

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
def get_computer_choice():
    from random import choice as c
    options = ["rock", "paper", "scissors"]
    compChoice = c(options) #pick one of three strings at random
    return compChoice

def get_player_choice():
    options = ["rock", "paper", "scissors"]
    #validate and obtain user choice
    userChoice = input("Choose rock, paper, or scissors: ")
    while userChoice not in options:
        print(f"You made an invalid choice. Please try again.")
        userChoice = input("Choose rock, paper, or scissors: ")
    return userChoice

def get_winner(compChoice, userChoice):
    #condition(s) for a win
    win = (((userChoice == "rock") & (compChoice == "scissors")) | ((userChoice == "paper") & (compChoice == "rock")) | ((userChoice == "scissors") & (compChoice == "paper")))
    if compChoice == userChoice:
        winner = str("tie")
    elif win == 1:
        winner = str("player")
    else:
        winner = str("computer")
    return winner

def main():
    compChoice = get_computer_choice()
    userChoice = get_player_choice()
    print(f"  The computer chose {compChoice}, and you chose {userChoice}.")
    result = get_winner(compChoice, userChoice)

    #repeat previous process if choices are the same
    while result == "tie":
        print(f"  Its a tie. Starting over.\n")
        compChoice = get_computer_choice()
        userChoice = get_player_choice()
        print(f"  The computer chose {compChoice}, and you chose {userChoice}.")
        result = get_winner(compChoice, userChoice)

    #result if user wins
    if result == "player":
        print(f"  {userChoice} beats {compChoice}")
        print(f"  You won the game!")
    #result if computer wins
    else:
        print(f"  {compChoice} beats {userChoice}")
        print(f"  You lost.  Better luck next time.")

    print(f"Thanks for playing.")

if __name__ == "__main__":
    main()
