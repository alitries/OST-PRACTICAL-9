#3. WAP for Calorie Counter as follows:


#Read the no of carbohydrates, proteins and fats for a given food item. Calculate the amount of energy in it as follows:
#1 carb = 4 calories
#1 protein = 4 calories
#1 fats = 9 calories

c=int(input("Enter the number of carbohydrates"))
p=int(input("Enter the number of protiens"))
f=int(input("Enter the number of fats"))
calories=0
print("calories=",c*4+p*4+f+9)
