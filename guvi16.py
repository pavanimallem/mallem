x=int(input(""))
y=int(input(""))
print("prime numbers between",x,"and",y,"are")
for n in range(x,y+1):
	if n>1:
		for i in range(2,n):
			if(i%n)==0:
		     break
	else:
	       	print("prime numbers")
