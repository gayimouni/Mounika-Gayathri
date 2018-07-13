print("enter the string number:")
a=int(input())
print("enter the ending number:")
b=int(input())
for m in range(a+1,b):
    n=str(m)
    l=len(n)
    sum=0
    for i in range(0,1):
        u=n[i]
        v=(int(u))**3
        sum +=v
    if sum==int(n):
        print(n)
