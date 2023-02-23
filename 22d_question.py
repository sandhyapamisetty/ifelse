a=int(input("enter the year"))
b=int(input("enter the salary"))
if a>5:
    c=a-5
    print(b+c*100)
elif a<5:
    print("no bonus")    
else:
    print("enter vlid data")