#part 6
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5


n = int(input("Enter the number of lines: "))

if (n < 1):
    print("The number of lines must not be less than 1")
else:
    for i in range(n):
        for j in range(n - i):
            print(n - j, end=" ")
        print()
