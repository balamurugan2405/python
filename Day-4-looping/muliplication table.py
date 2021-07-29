x=int(input("WHICH TABLE U WANT"))
y=int(input("STARTING OF TABLE"))
z=int(input("ENDING OF TABLE"))
if y<z:
    for i in range(y,z+1):
        print(f"{i} x {x} ={i*x}")
    
else:
    for i in range(y,z-1,-1):
        print(f"{i} x {x} ={i*x}")
    
