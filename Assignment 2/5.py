def multLIST(listELEM):  
    prod = 1
    for i in listELEM:
        prod *= i  
    return prod  

lst=[] 
n=int(input("Enter number of elements : ")) 
for i in range(0,n): 
    element = int(input()) 
    lst.append(element)
    
print("product of elements in list is : ",multLIST(lst))
