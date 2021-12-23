n = int(input("Enter a number: "))

s = 0
f = 1

for i in range(1, n+1):
        f = f * i
        s += i/f
        print("The result of is ",s)
