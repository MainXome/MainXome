#Random Module to make computer choose a random number
import random 
#Computer Guessing and User Guessing
Computer_Random = random.randint(1,100)
#Make game look good
print("\033[1m"+"Welcome to Number Guesser"+"\033[0m")
print("_________________________")
#User Input
User_Guess = int(input("Enter a number from 1 to 100 "))

#Win Conditions
while True:
    if User_Guess > Computer_Random:
        print("The number chosen by the computer is lower")
        User_Guess = int(input("Enter a number from 1 to 100 "))
    
    if User_Guess < Computer_Random:
        print("The number chosen by the computer is higher")
        User_Guess = int(input("Enter a number from 1 to 100 "))
    if User_Guess == Computer_Random:
        print("Congratulations, You guessed the right number")
    
    




    
    
    
      
       
    
    
    
    
    
    
 
  
    
    
    
        
    

   