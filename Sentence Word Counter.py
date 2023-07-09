#Ask the user for the sentence
sentence = input("Enter a sentence: ")
words = sentence.split() #splits the sentence into its words
word_counts = {} 
for word in words: #counts the words in a sentence
    if word in word_counts:
        word_counts[word] += 1 #checks if there are same words in the sentence
    else:
        word_counts[word] = 1

