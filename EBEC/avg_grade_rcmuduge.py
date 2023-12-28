"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 02/26/2022

Description:
    This program displays the average score and letter grade for 5 individual scores and letter grades. 

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
def get_valid_score():
    score = float(input("Enter a score: "))
    #ask for input until valid score is entered
    while (score > 100) or (score < 0):
        print(f"  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    return score

def calc_average(scores):
    average = sum(scores) / len(scores) #average of scores matrix
    return average

def determine_grade(score):
    #grade letters based on grading scale
    if score >= 92:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 73:
        grade = "C"
    elif score >= 64:
        grade = "D"
    else:
        grade = "F"
    return grade

def main():
    score = [0.0, 0.0, 0.0, 0.0, 0.0] #initialize matrix to store scores
    #fill out matrix with user inputs
    for n in range (0,5): 
        score[n] = get_valid_score()
        grade = determine_grade(score[n])
        print(f"  The letter grade for {score[n]:.1f} is {grade}.")

    #calculate average score and determine letter grade
    avgScore = calc_average(score)
    avgGrade = determine_grade(avgScore)
    print(f"\nResults:")
    print(f"  The average score is {avgScore:.2f}.")
    print(f"  The letter grade for {avgScore:.2f} is {avgGrade}.")

if __name__ == "__main__":
    main()
