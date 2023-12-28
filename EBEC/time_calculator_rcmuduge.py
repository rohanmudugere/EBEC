"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 02/12/2022

Description:
    This program calculates time in days, hours, minutes, and seconds given a time in seconds.

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

    #initialize variables
    seconds = 0
    minutes = 0
    hours = 0
    days = 0

    #calculate variables based on time input in seconds
    time = float(input("Please enter a time in seconds: "))
    if time < 60:
        print(f"  {time:,.0f} seconds is less than one minute.")
    elif (time < 3600):
        minutes = time // 60
        seconds = time % 60
    elif (time < 86400):
        hours = time // 3600
        minutes = time % 3600 // 60
        seconds = time % 3600 % 60
    else:
        days = time // 86400
        hours = time % 86400 // 3600
        minutes = time % 86400 % 3600 // 60
        seconds = time % 86400 % 3600 % 60

    #display calculations based on conditions
    if days == 0 and hours == 0 and minutes != 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {minutes:.0f} minute(s) and {seconds:.0f} second(s).")
    elif days == 0 and hours == 0 and minutes != 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {minutes:.0f} minute(s).")
    elif days == 0 and hours != 0 and minutes != 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {hours:.0f} hour(s), {minutes:.0f} minute(s) and {seconds:.0f} second(s).")
    elif days == 0 and hours != 0 and minutes == 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {hours:.0f} hour(s) and {seconds:.0f} second(s).")
    elif days == 0 and hours != 0 and minutes != 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {hours:.0f} hour(s) and {minutes:.0f} minute(s).")
    elif days == 0 and hours != 0 and minutes == 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {hours:.0f} hour(s).")
    elif days != 0 and hours != 0 and minutes != 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s), {hours:.0f} hour(s), {minutes:.0f} minute(s) and {seconds:.0f} second(s).")
    elif days != 0 and hours == 0 and minutes != 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s), {minutes:.0f} minute(s) and {seconds:.0f} second(s).")
    elif days != 0 and hours == 0 and minutes == 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s) and {seconds:.0f} second(s).")
    elif days != 0 and hours == 0 and minutes != 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s) and {minutes:.0f} minute(s).")
    elif days != 0 and hours != 0 and minutes == 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s) and {hours:.0f} hour(s).")
    elif days != 0 and hours != 0 and minutes != 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s), {hours:.0f} hour(s) and {minutes:.0f} minute(s).")
    elif days != 0 and hours != 0 and minutes == 0 and seconds != 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s), {hours:.0f} hour(s) and {seconds:.0f} second(s).")
    elif days != 0 and hours == 0 and minutes == 0 and seconds == 0:
        print(f"  {time:,.0f} seconds equals {days:.0f} day(s).")    

if __name__ == "__main__":
    main()
