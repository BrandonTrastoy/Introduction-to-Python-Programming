#===================================================================================
#Author: Brandon Trastoy
#Title: The Disk Of Chance
#Description: A game against chance. If the user selects the correct side
#            of the coin, then he wins. If he chooses the incorrect side,
#            then he loses. All wins and losses will be added and then
#            used to calculate user win percentage.
#===================================================================================

#Since this program is using a random function we will need to import it's library
#===================================================================================
import random
#===================================================================================

#Saving wins as 0
win = 0
#Saving losses as 0
loss = 0

#This loop will allow the game to return back to the MAIN MENU upon user input
initial = 0
while initial == 0:


    #This is the games MAIN MENU, the user will be allowed to choose from the 3 choices
    #===================================================================================
    print("Disk of Chance")
    print(" ")
    print("MAIN MENU: ")
    print("Enter 1 for story mode")
    print("Enter 2 for normal Heads or Tails.")
    print("Enter 3 to quit.")
    #Saves user input in variable name, choice. This variable will determine which part of the game the user will play
    choice = eval(input("Enter Your Choice Here: "))
    #===================================================================================
    
    #Added white space for legibility purposes
    print(" ")


#==========================================================================================
#==========================================================================================
#                                After this point is choice 1
#==========================================================================================
#==========================================================================================



    #If choice is equal to 1, then the game will begin the story mode section
    if choice == 1:

        #Prints title
        print("[-------------------------------------------------The Disk of Chance!--------------------------------------------------]")

        #Plot Dialogue
        #===================================================================================
        print("     The year is 2125, and the world has been taken over by a highly intelligent alien race. At first, the humans")
        print("believed that the game the new invaders played was a joke. However, to them it was reality, that those with luck")
        print("should rule over all. We tried to beat them at their own game, but it seems luck was not on our side. We tried ")
        print("to ignore their rules and attack them before they attacked us, but it seems there was a hidden rule we did not")
        print("know. That those who play and lose to their misfortune from the disk of chance our bound to the victor. In an")
        print("instant we lost all our freedom, but we still fight. We fight, people risking their own freedom for the chance they")
        print("may free this world. Every month a challenge is held, one human is allowed to play the game to regain this worlds")
        print("freedom. To this day we have not won, but we still have hope. We have been testing each humans luck by means")
        print("of probability. Then one day we found you, your luck slightly tipped the scale in your favor, higher than any one")
        print("before you. We have found hope in you.")
        #===================================================================================

        
        print(" ")


        #Saves user input in variable name, secondChoice
        secondChoice = input("Will you help us regain our freedom? YES or NO: ")
        print(" ")
        #This line will uppercase all characters in secondChoice
        secondChoice = secondChoice.upper()
        #If user input is equal to yes, then the game will continue to run
        if  secondChoice == "YES" or secondChoice == "Y" or secondChoice == "YE":
            
            
            #Dialogue to progress the plot
            #===================================================================================
            print("Thank you traveler for accepting this quest. What is your name?")
            userName = input("Name: ")
            print(userName, ", a name fit for our savior. So shall it be written in our history books.")

            print(" ")
            print("Ok, enough talk, we need to re-test your win percentage.")
            print("If your win percentage is less than 50% out of 5 games you will not be able to compete.")

            print(" ")
            print("Welcome to the practice test.")
            print("In this game there are two choices, heads or tails. There is no right or wrong answer until the coin is tossed.")
            #===================================================================================

            #Another loop 
            sentinel = 0
            while sentinel == 0:

                
                #Literally just two spaces, and asks the user to press enter to further the game, 
                print(" ")
                justEnter = input("Press Enter to Begin: ")
                print(" ")

                #Redefines loop to be zero so the user can retry with fresh stats
                win = 0
                loss = 0
                
                #And another loop here too
                practice = 1
                while practice == 1:

                    #===================================================================================
                    #Saving user input in variable name, randomNum
                    randomNum = random.randint(0, 1)
                    #Saving user input in variable name, userInput
                    userInput = eval(input("Enter 0 for heads and 1 for tails: "))
                    #===================================================================================


                    #===================================================================================
                    #This if runs when the users answer mathces the random integer
                    if userInput == randomNum:
                        #If the user wins, then add 1 to win and save it
                        win = win + 1
                    #Otherwise ...       
                    else:
                        #Add 1 to my loss streak
                        loss = loss + 1
                    #===================================================================================


                    #Prints: wins, losses, and win to loss ratio
                    #===================================================================================
                    print("Wins:", win)
                    print("Losses:", loss)
                    totalGames = win + loss
                    winPercent = round(win / totalGames * 100, 2)
                    print("Win Percentage:", winPercent, "%")
                    #===================================================================================

                    #If total games equal to 5, stop loop
                    if totalGames == 5:
                        break
                    
                #If winPercent is greater than or equal to 50, then continue game                   
                if winPercent >= 50:
                    print("Your luck is excellent.")
                    print(" ")
                    
                    #Asks the user if they want to continue to the last fight
                    finalBoss = input("Do you wish to continue the game? YES or NO: ")
                    #Upper cases all characters in finalBoss variable
                    finalBoss = finalBoss.upper()

                    #If the user inputs yes, then the games continues to the boss fight
                    if finalBoss == "YES" or finalBoss == "Y" or finalBoss == "YE":
                    

                        #Just even more dialogue
                        print("Several Hours Later ...")
                        print("It's time to challenge them, step forward.")
                        print(" ")

                        #   **NEW**   Alien Speaks for first time, some how he/she knows English
                        print(" **Alien Speaking** : It's time to meet your fate. If you lose we will take your freedom, however if you win we will leave this planet.")
                        #Alien asks user if he agrees to terms, ((when looking for the else, known it is pretty far down this code)) saved in variable name otherChoice
                        otherChoice = input("Do you agree? YES or NO: ")
                        #Upper cases all characters in otherChoice
                        otherChoice = otherChoice.upper()

                        #If otherChoice is equal to yes, then the user will finally face the boss
                        if otherChoice == "YES" or otherChoice == "Y" or otherChoice == "YE":

                            #And here's some more ...
                            print("Okay, you agreed.")
                            print("Now we will begin")
                            print(" ")

                            
                            #Another...
                            print("{There will be 5 matches, first to get 3 correct out of 5 will win.}")
                            print(" ")
                            

                            #This is just another pause for the user
                            enter = input("Press enter when you're ready: ")
                            print(" ")

                            
                            #Here I redefine the wins and losses, this was solely for the purpose of not using the same wins and losses as the ones in practice
                            win = 0
                            loss = 0
                            totalGames = 0

                            #Ran out of names for my loops, this one is mach                        
                            mach = 0
                            while mach == 0:

                                #As you will notice, I reused this code a few times
                                #===================================================================================
                                #Saving user input in variable name, randomNum
                                randomNum = random.randint(0, 1)
                                #Saving user input in variable name, userInput
                                userInput = eval(input("Enter 0 for heads and 1 for tails: "))
                                #===================================================================================


                                #===================================================================================
                                #This if runs when the users answer mathces the random integer
                                if userInput == randomNum:
                                    #If the user wins, then add 1 to win and save it
                                    win = win + 1
                                #Otherwise ...       
                                else:
                                    #Add 1 to my loss streak
                                    loss = loss + 1
                                #===================================================================================

                                    
                                #Tells the user there wins and losses after every try
                                print("Wins:", win)
                                print("Losses:", loss)
                                
                                
                                #If the user wins the three games, then all this useless dialogue will appear
                                #===================================================================================
                                if win >= 3:

                                
                                    print(" ")
                                    
                                    print("You have won this worlds freedom back.")
                                    print("Your name will be written in all our history books as I promised.")
                                    print("Aswell as that, we wish to grant you the finest this world has to offer.")
                                    print("Thank you again, this planet is in your hands.")
                                    print("THE END")
                                    
                                    print(" ")
                                    print(" ")

                                    print(" CREDITS: ")
                                    print(" Story and Design: Brandon Trastoy")
                                    print(" Text Actors: Brandon Trastoy")
                                    print(" Soundless Music: Brandon Trastoy")
                                    print(" Everything Else: Brandon Trastoy")
                                    
                                    print(" ")
                                    print(" Special Thanks to Brandon Trastoy")
                                    print(" ")
                                    
                                    #Prompts the user to press enter to return to Main Menu, it would've done it anyways if this wasn't here
                                    enter = input("Press enter to return to MAIN MENU: ")
                                    #Falsifies the previous loops so the game is sent back to the MAIN MENU
                                    mach = 1
                                    sentinel = 1
                                #===================================================================================

                                
                               
                                #If the user losses the three games, then this useless dialogue will appear
                                #===================================================================================
                                elif loss >= 3:
                                    print("We are deeply sorry young traveler, you have lost.")
                                    print("You will now become the personal slave of the aliens.")
                                    print("Good Luck ... nevermind.")
                                    print("THE END")

                                    print(" ")
                                    print(" ")

                                    print(" CREDITS: ")
                                    print(" ......")
                                    print(" ..........")
                                    print(" ..............")
                                    print(" ..................")
                                    
                                    print(" ")
                                    print("Didn't you lose, you dont deserve to see the after credits. SHOOOO")
                                    print(" ")

                                    #Prompts the user to press enter to return to Main Menu, it would've done it anyways if this wasn't here
                                    enter = input("Press enter to return to MAIN MENU: ")
                                    #Falsifies the previous loops so the game is sent back to the MAIN MENU
                                    mach = 1
                                    sentinel = 1
                                #===================================================================================


                         #This is what happens if you disagree to the aliens terms                                   
                        else:
                            print("I do not hold it against you, however you should leave now before your dignity is destroyed.")
                            print(" .... BTW the planet gets destroyed")
                            print(" THE END")
                            enter = input("Press Enter to return to the MAIN MENU: ")
                            break

                    #This else goes with the if that asks the user if they want to continue after completing the practice, this sends user back to the MAIN MENU
                    else:
                        print("Okay, returning to MAIN MENU.")
                        break
                #==========================================================================================
                    
                        
                #Otherwise if winPercent is less than or 50, ask the user to retry or quit
                #==========================================================================================                       
                else:
                    #Just a simple comment for the user
                    print("Was the first time a fluke.")
                    print(" ")
                    #Asks the user if they want to try again or return the MENU
                    thirdChoice = eval(input("Enter 0 to try again, or enter 1 for Main Menu: "))
                    #If 0 the program will run again
                    if thirdChoice == 0:
                        sentinel = 0
                    #Otherwise, if 1 then the program will return to the main
                    elif thirdChoice == 1:
                        break

                
        #If the users input to secondChoice is equal to anything other than yes, then the game will ask to return to the MAIN MENU
        #==========================================================================================
        else:
            print("Thank you for your time, we wish you the best of luck in this world stripped of it.")
            print(" ")
            returnToMenu = input("Would you like to return to the MAIN MENU, YES or NO: ")
            returnToMenu = returnToMenu.upper()
            if returnToMenu == "YES" or returnToMenu == "Y" or returnToMenu == "YE":
                initial = 0
            #If user does not want to return to the MAIN MENU, then the game will stop running
            else:
                print(" ")
                print("Okay, Goodbye.")
                initial = 1
        #==========================================================================================


#==========================================================================================
#==========================================================================================
#                              After this point is choice 2
#==========================================================================================
#==========================================================================================

           

    elif choice == 2:
        while choice == 2:

            #===================================================================================
            #Saving user input in variable name, randomNum
            randomNum = random.randint(0, 1)
            #Saving user input in variable name, userInput
            userInput = eval(input("Enter 0 for heads and 1 for tails: "))
            #===================================================================================


            #===================================================================================
            #This if runs when the users answer mathces the random integer
            if userInput == randomNum:
                #If the user wins, then add 1 to win and save it
                win = win + 1
            #Otherwise ...       
            else:
                #Add 1 to my loss streak
                loss = loss + 1
            #===================================================================================
                

            #Prints: wins, losses, and win to loss ratio
            #===================================================================================
            print("Wins:", win)
            print("Losses:", loss)
            totalGames = win + loss
            winPercent = round(win / totalGames * 100, 2)
            print("Total Games:", totalGames)
            print("Win Percentage:", winPercent, "%")
            #===================================================================================

            
            #If statement that will ask the user if they want to continue playing after 10 games
            if totalGames % 10 == 0:
                print(" ")
                #Continue or not
                fourthChoice = input("Would you like to continue, YES or NO: ")
                #Upper cases all characters in fourthChoice
                fourthChoice = fourthChoice.upper()
                print(" ")

                #If the user does not wish to play any longer, then game will return to the MENU 
                if fourthChoice == "NO" or fourthChoice == "N":
                    print("Okay, returning to menu.")
                    choice = 0
                    



#==========================================================================================
#==========================================================================================
#                              After this point is choice 3
#==========================================================================================
#==========================================================================================


    #What you get when you choose choice 3
    else:
        #ENDS GAME
        print("Okay, thanks for stopping bye.")
        print("Goodbye!")
        initial = 1







        
