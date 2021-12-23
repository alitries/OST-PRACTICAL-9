#10
#a
#b a
#a b a
#b a b a
#a b a b a


n = int(input("Enter the number of lines: "))

if (n < 1):
    print("The number of lines must not be less than 1")
else:
    for i in range(n):
        for j in range(i + 1):
            if ((i + j) % 2 == 0):
                print("a", end=" ")
            else:
                print("b", end=" ")
        print()
