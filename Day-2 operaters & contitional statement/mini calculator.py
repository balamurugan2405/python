print("calculator")
print("1-add")
print("2-Substract")
print("3-Multiply")
print("4-root")
print("5-Divide")
print("6-reminder")
cal=int(input("Enter Choice(1-6):"))
if cal==1:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a+b
    print(f"{a+b}")
elif cal==2:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a-b
    print(f"{a-b}")
elif cal==3:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a*b
    print(f"{a*b}")
elif cal==4:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a**b
    print(f"{a**b}")
elif cal==5:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a/b
    print(f"{a/b}")
elif cal==6:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    c=a%b
    print(f"{a%b}")
else:
    print("Invalid choise")
