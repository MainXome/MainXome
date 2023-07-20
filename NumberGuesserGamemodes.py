import random

print("What gamemode do you want to play")
print("Choose '1' to guess the number, Choose '2' to make the computer guess the number and Choose '3' to exit")
user_gamemode = int(input())

#User Guesses Number
if user_gamemode == 1:
    Computer_Random = random.randint(1,100)
    print("\033[1m"+"Welcome to Number Guesser"+"\033[0m")
    
    User_Guess = int(input("Enter a number from 1 to 100 "))
    
    while User_Guess > Computer_Random:
        print("The number chosen by the computer is lower")
        User_Guess = int(input("Enter a number from 1 to 100 "))
    
    while User_Guess < Computer_Random:
         print("The number chosen by the computer is higher")
         User_Guess = int(input("Enter a number from 1 to 100 "))
   
    if User_Guess == Computer_Random:
        print("Congratulations, You guessed the right number")
        
        
#Computer Guesses Number   
if user_gamemode == 2:
    print("\033[1m"+"Welcome to Computer Guesser"+"\033[0m")
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
    
    
if user_gamemode == 3:
    print("Exiting Program")
    exit