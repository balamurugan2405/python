x=[]
for i in range(2):
    x.append([])
    for j in range(2):
        x[i].append(int(input()))
    print()
y=[]
for i in range(2):
    y.append([])
    for j in range(2):
        y[i].append(int(input()))
    print()
c=[[0,0,],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            c[i][j]+=x[i][k]*y[k][j]
            
for i in c:
    print(*i)
    
      
            
           
     
      
