import random

User_Number = int(input("Enter the number you want the computer to guess "))
Computer_Guesses = random.randint(1,100)
Computer_Guess_Prompt = print("Is the number" + " = " + str(Computer_Guesses))
User_Help = str(input("Type L for a lower guess or H for a higer guess or Y if the answer is correct (USE L/Y/H ONLY) ")).lower() 
Options = "l", "h", "y"

    


    

while True:
        
    if User_Help == "l":
        Lower_Guess = print(random.randint(0,User_Number))
        User_Help = input("Type L for a lower guess or H for a higer guess or Y if the answer is correct ").lower()     
    
    if User_Help == "h":
        Higher_Guess = print(random.randint(User_Number,100))
        User_Help = input("Type L for a lower guess or H for a higer guess or Y if the answer is correct ").lower() 
    
    if User_Help == "y":
        print("The computer guessed your number")
        break
    exit
    
      
    
    
    





       
        
        
        
        
        
    
    
    
    
    
  