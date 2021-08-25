balance=1000
pin=int(input("ENTER YOUR 4-Digit ATM pin"))
pasword=9876
if pin==pasword:
    print("welcome mam/sir")
    print("1-balance enquery")
    print("2-withraw amount")
    print("3-deposite amount")
    option=int(input("1-3 enter which one"))
    if option==1:
        print(balance)
    elif option==2:
        withraw=int(input("enter withraw amount"))
        balance=balance-withraw
        print("Collect Your Cash")
        print(f"your blance is {balance}")
        print(balance)
    elif option==3:
        dep=int(input("ENTER AMOUNT :"))
        balance=balance+dep
        print("sucessfully deposite")
        print(f" your balance is {balance}")
    else:
        print("ENTER 1-3")
else:
    print("wrong pin,Please enter correct PIN")
