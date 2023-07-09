import random #random module for random computer choice

choices = ['rock', 'paper', 'scissors']
player_choice = input("Rock/Paper/Scissors ")
computer_choice = random.choice(choices) #let the computer decide randomly from the choices variable

print("Player:", player_choice)
print("Computer:", computer_choice)

if player_choice == computer_choice: #if same choice then draw
    print("You both lostt")
elif (player_choice == 'rock' and computer_choice == 'scissors') or\
     (player_choice == 'paper' and computer_choice == 'rock') or\
     (player_choice == 'scissors' and computer_choice == 'paper'):
    print("Player Won") #player win conditions
else:
    print("Computer Win")#computer win conditions