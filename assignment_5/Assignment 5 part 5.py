#WAP in Python to display the following patterns:
#1

#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


n= int(input("Enter the number of lines: "))

if (n < 1):
    print("The number of lines must not be less than 1")
else:
    for i in range(1, n + 1):
        k = 0
        for j in range(i):
            k += 1
            print(k, end=" ")
        print()
