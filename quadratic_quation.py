print("Enter three numbers where these are quadratic equation value (like a,b and c): a*X*X + b*X +c = 0")
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
d=b*b-4*a*c
if d>0:
    print("Roots are real and unequal")
elif d<0:
    print("Roots are imagenary")
else:
    print("Roots are real and equal")    
print("d=",d)    