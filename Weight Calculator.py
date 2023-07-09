weight = int(input("Weight?")) #ask for weight
unit = input("(K)gs or (L)bs ") #ask for the unit
converter = weight * 0.45 #converts into kgs into pounds
converter_2 = weight / 0.45 #converts pounds into kg
if unit.upper() == "K": 
    print("Weight in Lbs " + str(converter_2)) #gives the answer in pounds if kg is selected as unit
else:
    print("Weight In Kg " + str(converter)) #gives the answer in kgs if pounds is selected as unit
 