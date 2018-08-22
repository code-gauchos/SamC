import time

myName="Sam"
myAge="16"
yourName=input("What is your name?")
yourAge=int(input("What is your age?"))

print("Hello",yourName)

#time.sleep(1)  

if yourAge>30:
    print("You are old")
else: 
    print("You are young")

#time.sleep(1)  

print("My name is ",myName)

#time.sleep(1)  

print("And I am ",myAge, "years old.")

#ask manager how much for 8gb ram
#ASK CUSTOMER how many sticks of 8gb ram
#print out customer's total order
#then calculate tax(@8%)
#print tax and grand total

print("Let's Build a PC that fits your budget. What setup type would you like? We offer the Budget Gamer, ")
bossPrice=float(input("What is the price of an 8gb stick of ram?"))

customerorder=float(input("How many 8gb sticks would you like?"))

print("Ok, so you would like",customerorder, "sticks of 8gb ram priced at",bossPrice)

totalPrice=(customerorder*(bossPrice))

tax=(totalPrice*(0.08))

grandTotal=totalPrice+tax

print("Your tax comes to $",round(tax,2))
print("Your total comes to $",round(grandTotal,2),"Thank you for your purchase.")
hereit