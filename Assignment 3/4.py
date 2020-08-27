def almost_there(n):
	return (abs(100-n) <= 10) or (abs(200-n) <= 10)
n1=int(input("Enter a number : \n"))
print(almost_there(n1))
