username = input("Username: ")
destination = input("Destination: ")
one_way_distance = float(input("One-way distance in miles: "))
vehicles_mpg = float(input("Vehicles miles per gallon: "))
gas_price = float(input("Gas Price per gallon: "))
number_of_travelers = int(input("Number of travelers: "))

iTotalMiles = one_way_distance * 2
iTotalGas = iTotalMiles / vehicles_mpg
iGasCost = iTotalGas * gas_price
iCost_Per_Traveler = iGasCost / number_of_travelers

print("")
print("===================")
print(("Road Trip Planner").upper())
print("===================")
print("Traveler: " + username)
print(f"Destination: {destination}" )
print("Gas Cost: " + str(iGasCost))
print("Cost Per Traveler: " + str(iCost_Per_Traveler))
print("==================")
print("")