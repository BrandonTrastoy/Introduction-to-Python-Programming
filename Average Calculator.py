#====-.-=============-.-=============-.-==============-.-==========-.-====
#Author: Brandon Trastoy
#AverageCalculator.py, calculating 3 test grades and finding average
#====-.-=============-.-=============-.-==============-.-==========-.-====

#Program Header, introduce program
#====-.-=============-.-=============-.-==============-.-==========-.-====
print('====-.-=============-.-=============-.-===========-.-==========-.-====')
print('====-.-==========      TEST GRADE CALCULATOR      =============-.-====')
print('====-.-=============-.-=============-.-===========-.-==========-.-====')
#====-.-=============-.-=============-.-==============-.-==========-.-====


#Using while loop to make program run continuously until satisfied. 
#====-.-=============-.-=============-.-==============-.-==========-.-====
initial  = 0
while initial == 0:
#====-.-=============-.-=============-.-==============-.-==========-.-====

    print(' ')
    
#Prompting user to input grades  
#====-.-=============-.-=============-.-==============-.-==========-.-====
    #Promting user to enter the first grade
    grade1 = eval(input('Enter a value for grade 1: '))
    while grade1 >100 or grade1< 0:
            print('Invalid input, enter a grade between 0 and 100')
            grade1 = eval(input('Re-enter a value for grade 1: '))
    #Promting user to enter the second grade           
    grade2 = eval(input('Enter a value for grade 2: '))
    while grade2 >100 or grade2< 0:
            print('Invalid input, enter a grade between 0 and 100')
            grade2 = eval(input('Re-enter a value for grade 2: '))
    #Promting user to enter the third grade
    grade3 = eval(input('Enter the final grade, or grade 3: '))
    while grade3 >100 or grade3< 0:
            print('Invalid input, enter a grade between 0 and 100')
            grade3 = eval(input('Re-enter a value for grade 3: '))
#====-.-=============-.-=============-.-==============-.-==========-.-====    


#Calcuates the average of the three grades, saved in average
#====-.-=============-.-=============-.-==============-.-==========-.-====
    average = (grade1 + grade2 + grade3) / 3
#====-.-=============-.-=============-.-==============-.-==========-.-====
    

#Display grade
#====-.-=============-.-=============-.-==============-.-==========-.-====
    while average >100 or average< 0: 
        print('Invalid Average, enter numbers between 0 and 100')

    print ('Your average is', average)
    if average > 89 and average <= 100:
        print ('You earned an A',end="\n")
        print ('Congratulations, you\'re amazing.')
    elif average > 79 and average <= 89:
        print ('You earned an B' ,end="\n")
        print('Good Job')
    elif average > 69 and average <= 79:  
        print ('You earned a C' ,end="\n")
        print('You almost had a B, try harder next time')
    elif average > 59 and average <= 69:  
        print ('You earned a D' ,end="\n")
        print('You almost had a C, try harder next time')
    else:
        print('You failed.')
        print ('Good luck next time!')
#====-.-=============-.-=============-.-==============-.-==========-.-====    

        
                
#Lets the user confirm that they want to evaluate another grade
#====-.-=============-.-=============-.-==============-.-==========-.-====
    initial = eval(input('\nEnter 0 to continue, and anything else to stop: '))
#====-.-=============-.-=============-.-==============-.-==========-.-====







    
