def min(a, b, c):

 if (a <= b) and (a <= c):
  smallest = a

 elif (b <= a) and (b <= c):
   smallest = b
 else:
   smallest = c

 return smallest


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

print(min(a, b, c))
