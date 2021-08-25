x=[]
for i in range(3):
    x.append([])
    for j in range(3):
        x[i].append(int(input()))

for i in range(3):
    for j in range(3):
        print(x[j][i],end=" ")
    print()
for i in range(3):
    for j in range(3):
        print(x[i][j],end=" ")
    print()



    
     
