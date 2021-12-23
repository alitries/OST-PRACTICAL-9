n = int(input("Enter the number of lines "))

if (n<1):
    print("The number of lines should not be less than 1")
else:
    for i in range(n):
        for j in range(i + 1):
            if ((i + j) % 2 == 0):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
