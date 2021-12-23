#WAP to display the sum of all numbers between a and b which are divisible both by 3 or 7


a=int(input("Enter a"))
b=int(input("Enter b"))

s=0
for i in range(a,b+1):
    if(i%3==0 or i%7==0):
        print(i)
        s=s+i
print("The summation is ",s)
