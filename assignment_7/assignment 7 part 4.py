#while loop
#to calculate 1*2+2*3+3*4+....+n*n+1

n=int(input("Enter n: "))
s=0
i=1
while(i<=n):
     s=s+i*(i+1)
     i=i+1
print("The summation is ",s)
