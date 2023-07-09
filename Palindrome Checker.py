word = input(str("Enter a word "))
lowercase = (word.lower()) #turns the entered sentence into lowercase
reverse_word = (lowercase [::-1]) #writes the word in reverse order
if reverse_word == lowercase: #checks if reverse word if equal to unreversed word
    print("This word is a palindrome")
elif reverse_word != lowercase:
    print("This word is not a palindrome")
