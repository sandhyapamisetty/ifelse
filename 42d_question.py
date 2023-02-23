#                             mobile number

a= int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>=100 and a<=999:
    print("+,("+str (a)+")", end ="") 
if b>=100 and c<=10000:
    print(b,end=" ")
if c>=100 and c<=10000:
    print(c,end=" ")
else:
    print("no")