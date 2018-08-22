import time

myName="Sam"
myAge="16"
yourName=input("What is your name?")
yourAge=int(input("What is your age?"))

print("Hello",yourName)

time.sleep(3)  

if yourAge>30:
    print("You are old")
else: 
    print("You are young")

time.sleep(3)  

print("My name is ",myName)

time.sleep(3)  

print("And I am ",myAge, "years old.")

yourPrice=float(input("What is your price?"))

yourPrice=yourPrice+(yourPrice*0.08)

print("$",yourPrice)