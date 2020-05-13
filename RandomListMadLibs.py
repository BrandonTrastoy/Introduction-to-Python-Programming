#=================================================================
#Author: Brandon Trastoy
#RandomListMadLibs.py
#Description: This program chooses a random grade, student, class, and professor
#                    and then places it in the print statement below
#=================================================================

import random

#Loops the program
initial = 0
while initial == 0:

    # List of 9 possible grades
    grades = ["A","A-","B+","B","B-","C+","C","D","F"]

    # Chooses one grade from the grades list 
    randGrade = grades[random.randint(0,8)]

    # List of 7 student names
    students = ["Brandon", "Mo", "Tim", "Collins", "Ramon", "Pablo", "Dawud"]

    # Chooses a random student name from the student list
    studentName = students[random.randint(0,6)]

    # List of 5 class names
    classes = ["CIS - 108", "MA -101", "EC - 101", "HI - 101", "MA - 109"]

    # Chooses a random class name from the classes list
    className = classes[random.randint(0,4)]

    # List of 4 professor's names
    professors = ["Cameron", "Collins", "Corpus", "Cohen"]

    # Chooses a random professor name from the professors list
    profName = professors[random.randint(0,3)]

    # Varible names: studentName, className, profName, randGrade; are randomized and input into the statement 
    print("This semester,",studentName,"signed up for",className)
    print("The professor for this class was Professor",profName)
    print("This professor has a reputation for being difficult.")
    print("How did our student do? Well, they received a grade of ",randGrade)

    # Just a space
    print(" ")
    
    # Ask the user to enter 0 or 1: 0 = continue, 1 = stop
    runAgain = eval(input("Enter 0 to try again, or Enter 1 to stop program: "))

    # Another space
    print(" ")

    # If runAgain = 1, the program will terminate
    if runAgain == 1:
        initial = 1

    
