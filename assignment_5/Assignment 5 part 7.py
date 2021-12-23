#7th
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1


n = int(input("Enter the number of lines: "))

if (n < 1):
    print("The number of n must not be less than 1")
else:
    for i in range(n):
        for j in range(n - i):
            print(n - i, end=" ")
        print()
