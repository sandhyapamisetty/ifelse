#           librariry question


a=int(input("expected day"))
b=int(input("expected month"))
c=int(input("expected year"))
d=int(input("return  day"))
e=int(input("return month"))
f=int(input("return year"))
if d<=a and e==b and f==c:
    print("no charge")
elif d>a and e==b and f==c:
    print((d-a)*15)
elif d>a and e>b and f==c:
    print((d-a)*15+(e-b)*500)
elif f>c:
    print("fine",10000) 
else:
    print("no")