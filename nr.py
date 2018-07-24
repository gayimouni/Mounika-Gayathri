h=int(input())
rev=0
while(h>0):
    dig=h%10
    rev=rev*10+dig
    h=h//10
print(rev)
