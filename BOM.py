import json
import Product

jsonFile = open("./machine.json")

machine = json.load(jsonFile)

print("Let's Build a PC that fits your budget. What setup type would you like? We offer the Budget Gamer, the Mid Ranger, the Power Budget, and the All Out Power.")

products = []

for machineCounter in range(len(machine)):
    product = Product.Product()

    product.systemName = machine[machineCounter]["systemName"]
    product.systemPrice = machine[machineCounter]["systemPrice"]
    
    products.append(product)

    print(product.systemName)
    print(product.systemPrice)

    machineCounter+=1




#print("Ok, so you would like the", machines, "priced at $",price)


#tax=(price*(0.08))

#grandTotal=totalPrice+tax

#print("Your tax comes to $",round(tax,2))

#print("Your total comes to $",round(grandTotal,2),"Thank you for your purchase.")
