st=input()
ls=list(st)
if ord(ls[0])>96:
	ls[0]=chr(ord(ls[0])-32)
for x in range(len(ls)-1):
	if ls[x]==' 'and ord(ls[x+1])>96:
		ls[x+1]=chr(ord(ls[x+1])-32)
an=''
for x in ls:
	an=an+x
print(an)
