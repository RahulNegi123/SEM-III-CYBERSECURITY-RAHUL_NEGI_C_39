print("Enter limit : \n")
limit=int(input())
res = {}

for possiblePrime in range(2, limit+1):
	isPrime = True
	for num in range(2, possiblePrime):
		if possiblePrime % num == 0:
			isPrime = False
	if isPrime:
		res[possiblePrime]="Prime"
		
	else:
		res[possiblePrime]="Non Prime"

print(res)
res1 = list(res.values())
key_list = list(res.keys()) 
len1=len(res1)

for i in range(0,len1):
        s=res1[i]
        if s=="Non prime":
        	res.pop(key_list[i])
                 
        

print("\n new updated dictionary after deletion\n")
print(res)
