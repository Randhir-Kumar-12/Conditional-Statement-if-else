
year=int(input("Enter the leap year:"))

if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Not leap year")
elif year%4==0:
    print("Leap year") 
else:
    print("Not leap year")               
