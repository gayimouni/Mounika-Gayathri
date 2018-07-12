n=int(inout("enter the number="))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==n):
    print("is a palindrom")
else:
    print("is not apalindrom")
