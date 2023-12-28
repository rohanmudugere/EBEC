"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 09.4 - File Analysis
Date: 04/08/2022

Description:
    This program finds the frequency of each word in a file, and then writes each word (in alphabetical order) with its frequency into a new file. 
    The program then determines which words are in both files and which words are exclusive to just one file or the other, and then writes 
    these words into their own respective files. 

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
from string import punctuation


punctuation

def main():
    #create list of words
    with open("python_1.txt") as file1:
        words1 = []
        for line in file1:
            wordsInLine1 = line.split(' ')
            words1 += wordsInLine1
    #create dictionary with words and frequencies
    with open("python_1_word_frequency.txt", "w") as file3:
        words1Dict = {}
        for i in range(len(words1)):
            words1[i] = words1[i].strip()
            words1[i] = words1[i].rstrip(punctuation).lstrip(punctuation)
            words1[i] = words1[i].lower()
            if words1[i] not in words1Dict:
                words1Dict[words1[i]] = 1
            else:
                words1Dict[words1[i]] += 1
        #alphabetize dictionary
        words1Aplh = dict(sorted(words1Dict.items()))
        #write the word and frequency on its own line
        for k, v in words1Aplh.items():
            file3.write(k + ": " + str(v) + "\n")

    #create list of words
    with open("python_2.txt") as file2:
        words2 = []
        for line in file2:
            wordsInLine2 = line.split(' ')
            words2 += wordsInLine2
    #create dictionary with words and frequencies
    with open("python_2_word_frequency.txt", "w") as file4:
        words2Dict = {}
        for i in range(len(words2)):
            words2[i] = words2[i].strip()
            words2[i] = words2[i].rstrip(punctuation).lstrip(punctuation)
            words2[i] = words2[i].lower()
            if words2[i] not in words2Dict:
                words2Dict[words2[i]] = 1
            else:
                words2Dict[words2[i]] += 1
        #alphabetize dictionary
        words2Aplh = dict(sorted(words2Dict.items()))
        #write the word and frequency on its own line
        for k, v in words2Aplh.items():
            file4.write(k + ": " + str(v) + "\n")

    with open("common_words.txt", "w") as file5:
        commonWords = []

    with open("eitherbutnotboth.txt", "w") as file6:
        exclusiveWords = []

if __name__ == "__main__":
    main()
