"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 03/39/2022

Description:
    This program converts letters to a phone number.  

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
def convert_number(input):
    #convert original values to numbers and add to new string 
    input = input.upper()
    phoneNum = str() 
    for i in range(len(input)):
        if (input[i] == "A") | (input[i] == "B") | (input[i] == "C"):
            phoneNum += "2"
        elif (input[i] == "D") | (input[i] == "E") | (input[i] == "F"):
            phoneNum += "3"
        elif (input[i] == "G") | (input[i] == "H") | (input[i] == "I"):
            phoneNum += "4"
        elif (input[i] == "J") | (input[i] == "K") | (input[i] == "L"):
            phoneNum += "5"
        elif (input[i] == "M") | (input[i] == "N") | (input[i] == "O"):
            phoneNum += "6"
        elif (input[i] == "P") | (input[i] == "Q") | (input[i] == "R") | (input[i] == "S"):
            phoneNum += "7"
        elif (input[i] == "T") | (input[i] == "U") | (input[i] == "V"):
            phoneNum += "8"
        elif (input[i] == "W") | (input[i] == "X") | (input[i] == "Y") | (input[i] == "Z"):
            phoneNum += "9"
        else:
            phoneNum += input[i]
    return phoneNum

def main():
    phoneNum = str(input("Enter a telephone number: ")) #get user-input
    print(f"The phone number is {convert_number(phoneNum)}") #display converted number

if __name__ == "__main__":
    main()
