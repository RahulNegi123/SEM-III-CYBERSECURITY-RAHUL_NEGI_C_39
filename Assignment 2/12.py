print("Enter limit : \n")
limit=int(input())

print("[", end =" ")

for possiblePrime in range(2, limit+1):
	isPrime = True
	for num in range(2, possiblePrime):
		if possiblePrime % num == 0:
			isPrime = False
	if isPrime:
		res = (possiblePrime,"Prime") 
	else:
		res = (possiblePrime,"Non Prime")
	if possiblePrime !=limit:
		print(res, "," , end =" ")
	else:
		print(res, end =" ")

print("]", end =" ")