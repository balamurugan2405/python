
x=[]
add=0
y=int(input("How many elements input"))
for i in range(0,y):
    x.append(int(input()))
    if x[i]%2==0:
        add+=x[i]
print(f" even number total is-{add}")
