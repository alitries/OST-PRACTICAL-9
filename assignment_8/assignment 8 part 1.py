def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

print(maximum(a, b, c))

          

