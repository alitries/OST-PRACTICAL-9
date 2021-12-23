# WAP in Python to read the marks and display the Grade obtained
#   Grade Marks Grade Points

marks=float(input("Enter the Marks Obtained"))

if(marks>=80):
    print("O grade & 10 Grade points")
elif(marks>=70):
    print("A+ Grade & 9 Grade points")
elif(marks>=60):
    print("A Grade & 8 Grade points")
elif(marks>=55):
    print("B+ Grade & 7 Grade points")
elif(marks>=50):
    print("B Grade & 6 Grade points")
elif(marks>=45):
    print("C Grade & 5 Grade points")
elif(marks>=40):
    print("D Grade & 4 Grade points")
else:
    print("F Grade & 0 Grade points")
                
