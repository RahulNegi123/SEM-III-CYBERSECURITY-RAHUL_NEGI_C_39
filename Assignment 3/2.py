def calc(a,b):
 if a % 2 == 0 and b % 2 == 0:
  if a < b:
   return(a)
  else:
   return(b)

 else:
  if a > b:
   return(a)
  else:
   return(b)


num1=int(input("Enter first number : \n"))
num2=int(input("Enter second number : \n"))
answer=calc(num1,num2)
print(answer)
