x=int(input("ENTer THE LAST NUMBER"))
y=int(2)
print(f"PRIMARY NUMBERS {y} to {x}:")
for i in range(y,x+1):
    if i>0:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)

