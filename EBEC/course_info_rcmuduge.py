"""
Author: Rohan Mudugere, rcmuduge@purdue.edu
Assignment: 09.3 - Course Info
Date: 04/07/2022

Description:
    This program displays the information for a given class. 

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
def get_course_data():
    #create nested dictionary with appropriate values
    classes = {}
    classes["CS101"] = {"room": "3004", "instructor": "Django", "time": "9:00 a.m."}
    classes["CS102"] = {"room": "4501", "instructor": "Idle", "time": "10:00 a.m."}
    classes["CS103"] = {"room": "6755", "instructor": "Rich", "time": "11:00 a.m."}
    classes["NT110"] = {"room": "1244", "instructor": "Marshal", "time": "12:00 p.m."}
    classes["CM241"] = {"room": "1411", "instructor": "Pickle", "time": "2:00 p.m."}
    return classes

def main():
    #get input and display appropriate values
    courses = get_course_data()
    course = input("Enter a course number: ")
    if ((course in courses) == True):
        courseInfo = courses.get(course)
        instructor = courseInfo.get("instructor")
        room = courseInfo.get("room")
        time = courseInfo.get("time")
        print(f"  The details for course {course} are:")
        print(f"    Instructor: {instructor}")
        print(f"          Room: {room}")
        print(f"          Time: {time}")
    else:
        print(f"  {course} is an invalid course number.")

if __name__ == "__main__":
    main()
