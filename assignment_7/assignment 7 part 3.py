#while loop

a=int(input("Enter a: "))
b=int(input("Enter b: "))

s=0
i=a
while(i<=b):
    if(i%8==0):
          s=s+i
    i=i+1
print("The summation is ",s)
