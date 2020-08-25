def unique_list(l):
    newLIST=[ ]
    for mem in l:
        if mem not in newLIST:
            newLIST.append(mem)
    return newLIST

lst=[] 
n=int(input("Enter number of elements : ")) 
for i in range(0,n): 
    element = int(input()) 
    lst.append(element)

print("\nOriginal list");
print(lst)

print("\nNew list with unique elements")
print(unique_list(lst))
