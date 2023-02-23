#                                ATM QUESTION

print("welcome to SBI bank")
print("please insert your card")
print("please selecte your language")
language=input("enter the language")
if language=="english":
    password=int(input("enter the password"))
    if password==1910:
        print("transactions/n  1. withdraw   2.balance enquairy 3.pin genaretion 4.deposite 5.exist")
        transaction=int(input("enter the transaction number"))
        amount=50000
        if transaction==1:
            withdraw=int(input("enter the withdraw"))
            if withdraw<=amount:
                print("collect your cash",withdraw)
                print("our remaining amount",amount-withdraw)
            else:
                print("not withdraw")
        elif transaction==2:
            print(amount)
        elif transaction==3:
            pingenaration=int(input("enter the pin genaration"))
            if pingenaration==pingenaration:
                print("new pin genaration succssfull")
            else:
                print("not correct")
        elif transaction==4:
            money=int(input("enter the money"))
            if money+amount:
                print("totalbalance is ",amount+money)
        elif transaction==5:
            exist=input("enter the exsit")
            if exist=="yes":
                print("thanks for your visiting")
            else:
                print("choose your transaction")
        else:
            print("choose correct value")
    else:
        print("correct password")
else:
    print("does not language")
                          