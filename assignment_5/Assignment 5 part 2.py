#2.
# # # # #(n-i+1)(5-1+1=5)
# # # #(5-2+1=4)
# # #(5-3+1=3)
# #(5-4+1=2)
#(5-5+1=1)
n=int(input("Enter the number of lines"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
     print("#",end=" ")
    print()
