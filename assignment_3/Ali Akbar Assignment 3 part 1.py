#WAP in Python to read 3 numbers and display the greatest of the 3

a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=int(input("Enter the 3rd number"))


if(a>b and a>c):
     print("The greatest number is ",a)
elif(b>c):
     print("The greatest number is ",b)
else:
     print("The greatest number is ",c)
