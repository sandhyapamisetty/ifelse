a=int(input("enter the maximum"))
b=int(input("enter the median"))
c=int(input("enter the minimum"))
if a>b and a<c:
    print("a is median")
elif b>a and b<c:
    print("b is median")
elif c>a and c<b:
    print("c is median")
else:
    print("no")