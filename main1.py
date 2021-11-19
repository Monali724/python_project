n=int(input())
for i in range(1,1+n//2):
	if(n==i*i):
		print("Perfect Square")
		break
else:
print("Not a perfect square")