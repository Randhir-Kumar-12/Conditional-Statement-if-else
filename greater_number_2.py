a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

#This is a optimize logic beuse it finds the greatest number in two steps
if a>b:
    if a>c:
        print("The greatest number=",a)
    else:
        print("The greatest number=",c)
elif b>c:
    print("The greatest number=",b)
else:
    print("The greatest number=",c)

#This is not optimize logic
if a>b and a>c:
        print("The greatest number=",a)
elif b>c and b>a:
        print("The greatest number=",b)
else:
    print("The greatest number=",c)



