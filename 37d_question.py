a=int(input("enter the year"))
b=int(input("enter the month"))
c=int(input("enter the days"))
if b>1 and b<12:
    if c>1 and c<31:
        print(a,"-",b,"-",c+1)
else:
    print("no")