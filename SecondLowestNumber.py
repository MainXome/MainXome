numbers = list(map(int, input("Enter numbers (separated by spaces): ").split()))
numbers.sort() #sorts the number entered by the unit
print("Second lowest =", numbers[1]) #selects the second number from the sorted numbers