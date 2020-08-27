def lesser_of_two_evens(a,b):
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
answer=lesser_of_two_evens(num1,num2)
print(answer)
