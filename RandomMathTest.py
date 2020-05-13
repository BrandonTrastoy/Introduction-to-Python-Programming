#Author: Brandon Trastoy
#Title: RandomNumberTest.py
#Description:
#Conducting a test for the user to answer three math questions. 
#Give user number and letter grade for test results.

#First things first, import math and random libraries
import math
import random

#Introduce user to program
#====-.-=============-.-=============-.-==============-.-==========-.-====
userName = input("What is your name? ")
print("Hello", userName, ", welcome to the \"Random Math Test\".")
print("You will be asked to answer three math questions and will be then graded at the end.")
#====-.-=============-.-=============-.-==============-.-==========-.-====

print(" ")

#Creating loop to give the user free will to quit the program before hand.
#====-.-=============-.-=============-.-==============-.-==========-.-====
initial = "yes"
userInput = input("Do you wish to continue, yes or no? ")
while initial == userInput:
#====-.-=============-.-=============-.-==============-.-==========-.-====

    print(" ")

    #Gigantic Sign whic has no actual mean but to look pretty
#====-.-=============-.-=============-.-==============-.-==========-.-====
    print("====-.-=============-.-=============-.-===========-.-==========-.-====") 
    print("====-.-=========            RANDOM MATH TEST              =============-.-====")
    print("====-.-=============-.-=============-.-===========-.-==========-.-====")
#====-.-=============-.-=============-.-==============-.-==========-.-====

    
    #Setting random intergers in variable names
#====-.-=============-.-=============-.-==============-.-==========-.-====
    randomNum1 = random.randint(1, 100)
    randomNum2 = random.randint(1, 100)
    randomNum3 = random.randint(1, 100)
#====-.-=============-.-=============-.-==============-.-==========-.-====

    
    #Correct answers  to test questions for the computer to use for comparison
#====-.-=============-.-=============-.-==============-.-==========-.-====
    #Question number 1 and answer saved in varible name correctAnswer1 
    #The if statement below is only needed for this problem
    correctAnswer1 = randomNum1 >= randomNum3
    if correctAnswer1 == True:
        correctAnswer1 = "true"
    else:
        correctAnswer1 = "false"
    #Question number 2 and answer saved in varible name correctAnswer2 
    correctAnswer2 = (randomNum2  * randomNum3 * randomNum1) / randomNum2
    #Question number 3 and answer saved in varible name correctAnswer3 
    correctAnswer3 = round(math.sqrt(randomNum3), 2)
#====-.-=============-.-=============-.-==============-.-==========-.-====

    print(" ")

    #Printing solve for users to know the test has begun.
#====-.-=============-.-=============-.-==============-.-==========-.-====
    print("*******************************SOLVE*******************************")

    #Question number 1 and user answer
    print("1)", randomNum1," greater than or equal to", randomNum3, ", true or false: ")
    answer1 = input("What is your answer to question 1? ")
    #Question number 2 and user answer
    print("2) What is (", randomNum2, "*",  randomNum3, "*", randomNum1, ")", "/", randomNum2)
    answer2 = eval(input("What is your answer to question 2? "))
    #Question number 3 and user answer
    print("3) What is the square root of", randomNum3,". Round to the second decimal place if needed.")
    answer3 = eval(input("What is your answer to question 3? "))
#====-.-=============-.-=============-.-==============-.-==========-.-====

    print(" ")
    print(" ")

    #Prints the correct answers of the problems to the user
#====-.-=============-.-=============-.-==============-.-==========-.-====
    print("******************************RESULTS******************************")

    #Prints correct or incorrect answer for question 1
    if answer1 == correctAnswer1:
        print("Your answer to question 1 was correct!")
        answerValue1 = 100
    else:
        print("Your answer to question 1 was incorrect.")
        print("     The correct answer is", correctAnswer1)
        answerValue1 = 0

    #Prints correct or incorrect answer for question 2
    if answer2 == correctAnswer2:
        print("Your answer to question 2 was correct!")
        answerValue2 = 100
    else:
        print("Your answer to question 2 was incorrect.")
        print("     The correct answer is" , correctAnswer2)
        answerValue2 = 0

    #Prints correct or incorrect answer for question 3
    if answer3 == correctAnswer3:
        print("Your answer to question 3 was correct!")
        answerValue3 = 100
    else:
        print("Your answer to question 3 was incorrect.")
        print("     The correct answer is", correctAnswer3)
        answerValue3 = 0
#====-.-=============-.-=============-.-==============-.-==========-.-====

    print(" ")
    print(" ")

    #Test Score function
#====-.-=============-.-=============-.-==============-.-==========-.-====
    testScore = round((answerValue1 + answerValue2 + answerValue3)/ 3,  2)
#====-.-=============-.-=============-.-==============-.-==========-.-====


    #GRADE
    #Yes, I do know that there is no possibility of getting a B or C on this test, but it doesn't hurt
    # to be prepared for any changes.
#====-.-=============-.-=============-.-==============-.-==========-.-====
    if testScore >= 90:
        print("Your score is", testScore, ". You got an A!")
        print("     Woooooow, you're amazing.")
    elif testScore >= 80:
        print("Your score is", testScore, ". You got a B.")
    elif testScore >= 70:
        print("Your score is", testScore, ". You got a C.")
        print("     Try harder next time.")
    elif testScore >= 60:
        print("Your score is", testScore, ". You got a D")
        print("     You need to brush up on your math a bit.")
    else:
        print("Your score is", testScore, ". You failed.")
        print("     Go back to school.")
#====-.-=============-.-=============-.-==============-.-==========-.-====
        
    print(" ")

    #The End? or The Beginning?
#====-.-=============-.-=============-.-==============-.-==========-.-====
    userInput = input("Would you like to try again, yes or no? ")
    if userInput == "no":
        print("Thanks for taking the test, I hope you learned something from it.")
        print("Good bye.")
        break
#====-.-=============-.-=============-.-==============-.-==========-.-====        
        
#END OF PROGRAM        
 



          
