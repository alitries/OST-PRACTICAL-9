#WAP in Python to read the units consumed and calculate the electricity charges


units=int(input("Enter the number of units consumed"))

if(units<=100):
    charges=units*5
elif(units<=300):
   charges=100*5+(units-100)*7
elif(units<=500):
    charges=100*5+200*7+(units-300)*10
else:
    charges=100*5+200*7*10+(units-500)*15
print("The electricity charges are ",charges)

          
