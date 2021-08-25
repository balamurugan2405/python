n=[]
x=int(input("how many elements input your list:"))
for i in range(0,x):
    y=int(input())
    n.append(y)
for i in n:
    temp = i
    sum = 0
    while(temp):
        rem = temp % 10
        sum += n(rem)
        temp = temp // 10
        
   
