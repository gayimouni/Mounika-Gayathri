x=int(input())

prime=1

i=2

while i<x:

	if(x%i==0):

		prime=0

	i=i+1	

if(prime==1):

	print("prime")

else:

	print("not")
