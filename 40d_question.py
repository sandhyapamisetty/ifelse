age=int(input("enter the age"))
gender=input("enter the gender")
day=int(input("enter the day"))
if age>=18 and age<30:
    gender=="m"
    wage=700*day
    print("total",wage)
elif age>=18 and age<30:
    gender=="f"
    wage=750*day
    print("total",wage)
elif age>=30 and age<40:
    gender=="m"
    wage=800*day
    print("total",wage)
elif age>=30 and age<40:
    gender=="f"
    wage=850*day
    print("total",wage)
else:
    print("no")
    