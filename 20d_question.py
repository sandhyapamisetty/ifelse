basicsalary= int(input("enter the number"))
if basicsalary<=10000:
    HRA20/100*basicsalary
    DA80/100*basicsalary
    print(HRA+DA+basicsalary)
elif basicsalary<=20000:
    HRA25/100*basicsalary
    DA90/100*basicsalaty
    print(HRA+DA+basicsalary)
elif basicsalary>2000:
    HRA30/100*basicsalary
    DA95/100*basicsalary
    print(HRA+DA+basicsalary)
else:
    print("no salary")    