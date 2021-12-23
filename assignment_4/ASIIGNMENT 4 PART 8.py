# 8
#; * # * #
#;* # * #
#;# * #
#;* #
#;#


n = int(input("Enter the number of lines: "))

if (n < 1):
    print("The number of lines must not be less than 1")
else:
    for i in range(n):
        for j in range(n - i):
            if ((i + j) % 2 == 0):
                print("#", end=" ")
            else:
                print("*", end=" ")
        print()
