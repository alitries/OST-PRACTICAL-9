def sumofalldigits (number):
    sum=0
    for digit in str(number):
        sum += int(digit)
    return sum

n=int(input("Enter a number: "))
print(f"The sum of all digits is {sumofalldigits(n)}")
