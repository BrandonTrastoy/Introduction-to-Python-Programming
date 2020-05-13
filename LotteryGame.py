#====================================================================
#====================================================================
#Authors: Brandon Trastoy
#Title: The Lottery Game
#Description: This program will generate a random number and compare it to the users input. 
#====================================================================
#====================================================================

#Importing random library
import random

#Introduces user to program and greets them
#====================================================================
userName = input("What is your name? ")
print("Hello,", userName, "welcome to the lottery game. It isn't easy to hit the jackpot.")
#====================================================================

#Loop to make the program run continuously unless told otherwise
#====================================================================
userAnswer = input("Do you wish to continue, yes or no: ")
userAnswer2 = userAnswer.lower()
initial = "yes" 
while initial == userAnswer2:
#====================================================================

    #Setting variables 
#====================================================================
    #Generating random number and saving it in variable name, randomNum
    randomNum = random.randint(100,999)
    #Getting user input and saving it in variable name, userInput
    userInput = eval(input("Enter a three digit number: "))
#====================================================================

    #Function to find each individual number of userInput
#====================================================================
    #Finds value in the hundredths place
    x = userInput // 100
    #Finds value in the tenths place
    y = userInput // 10 % 10
    #Finds value in ones place
    z = userInput % 10
#====================================================================

    #Function to find each individual number of randomNum
#====================================================================
    #Finds value in the hundredths place
    x2 = randomNum // 100
    #Finds value in the tenths place
    y2 = randomNum // 10 % 10
    #Finds value in ones place
    z2 = randomNum % 10
#====================================================================

    #Reorganizes value of userInput to allow for multiple variations 
#====================================================================    
    #xzy
    a1 = (x*100 + z*10 + y)
    #yzx
    a2 = (y*100 + z*10 + x)
    #yxz
    a3 = (y*100 + x*10 + z)
    #zxy
    a4 = (z*100 + x*10 + y)
    #zyx
    a5 = (z*100 + y*10 + x)
#====================================================================    

    #Reorganizes value of randomNum to allow for multiple variations
#====================================================================
    #xzy
    b1 = (x2*100 + z2*10 + y2)
    #yzx
    b2 = (y2*100 + z2*10 + x2)
    #yxz
    b3 = (y2*100 + x2*10 + z2)
    #zxy
    b4 = (z2*100 + x2*10 + y2)
    #zyx
    b5 = (z2*100 + y2*10 + x2)
#====================================================================
    
    print(randomNum)
    print(userInput)

    #Tells user their prize or if they lost
#====================================================================
    #Compares userInput to randomNum
    if userInput == randomNum:
        print("You won $10,000")
    #Compares all possible combinations with exception to original
    elif a1 in {b1, b2, b3, b4, b5} or a2 in {b1, b2, b3, b4, b5} or a3 in {b1, b2, b3, b4, b5} \
         or a4 in {b1, b2, b3, b4, b5} or a5 in {b1, b2, b3, b4, b5}:
        print("You won $5,000")
    #Two or one number mathces          
    elif x and y in {x2, y2, z2} or x and z in {x2, y2, z2} or y and z in {x2, y2, z2}:
        print("You won $500")
    
    elif x in {x2, y2, z2} or y in {x2, y2, z2} or z in {x2, y2, z2}:
        print("You won $1") 
    #Values do not match
    else:
        print("Ahhhhhhhhhhh, you lost")
#====================================================================
  
