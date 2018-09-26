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
    