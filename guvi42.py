s1,s2=map(str,raw_input().split())
p1=len(s1)
p2=len(s2)
if p1==p2:
	print s2 or s1
elif p1>p2:
	print s1
else:
	print s2
