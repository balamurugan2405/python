x=[]
total=0
for i in range(3):
    x.append([])
    for j in range(3):
        x[i].append(int(input()))
    print()
for i in range(3):
    for j in range(3):
        if (j==1) or (i==1):
            total+=x[i][j]
        else:
            print(" ",end=" ")
    print()
print(f"{total}")
