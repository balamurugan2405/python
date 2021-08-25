x=[]
for i in range(4):
    x.append([])
    for j in range(4):
        x[i].append(int(input()))
    print()
for i in range(4):
    for j in range(4):
        if (j==0)or(i==3):
            print(x[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
