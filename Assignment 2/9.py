import sys
n = int(sys.argv[1])

num2=1
num1=0
# 0 not included in series. 
for i in range(0, n): 
	print(num2,end=" ") 
	add=num1+num2 
	num1=num2 
	num2=add