n=[]
x=int(input("how many elements input your list:"))
for i in range(0,x):
    y=int(input())
    n.append(y)
for i in n:
    if i%2==0:
        print(i,end=" ")
        
    
