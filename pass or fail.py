print("Enter five subjects of marks out of 100:")
h=int(input("1. "))
e=int(input("2. "))
m=int(input("3. "))
p=int(input("4. "))
c=int(input("5. "))

if h>=33 and e>=33 and m>=33 and p>=33 and c>=33:
    print("Pass")
    per_cent=((h+e+m+p+e)*100)/500
    if per_cent>=60:
        print("First division")
    elif per_cent>=45:   
        print("Second division")
    else:
        print("Third division")
else:
    print("Fail")
    