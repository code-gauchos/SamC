import json

jsonFIle = open("./machines.json")

machines = json.load(jsonFIle)

print("Let's Build a PC that fits your budget. What setup type would you like? We offer the Budget Gamer, the Mid Ranger, the Power Budget, and the All Out Power.")

for machineCounter in range(len(machines)):
    machines[machineCounter]["systemName"]
    print(machines[machineCounter]["systemName"])




#print("Ok, so you would like the", machines, "priced at $",price)


#tax=(price*(0.08))

#grandTotal=totalPrice+tax

#print("Your tax comes to $",round(tax,2))
#print("Your total comes to $",round(grandTotal,2),"Thank you for your purchase.")