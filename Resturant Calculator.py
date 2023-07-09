cost_of_meal = float(input("How much did your meal cost? "))
tip_given = input("Enter the tip percentage: ")
print("\x1B[3m" + "Total Bill  " + "\x1B[0m")
print("______________________")
converter = float(cost_of_meal)
government_tax = float(cost_of_meal) / float(100) * 16
tip_calculator = float(cost_of_meal) / 100 * float(tip_given)
total_bill = cost_of_meal + government_tax + tip_calculator
cashback = float(cost_of_meal) / 100 * 5
if total_bill >= 4000:
    int(total_bill) - int(cashback)
    print("Cashback: " + str(cashback))
    
print("Government Tax = 16%")
print("Tip Amount = " + str(tip_calculator))
print("Meal Cost = " + str(cost_of_meal))
print("Total Bill Amount = " + str(total_bill))

