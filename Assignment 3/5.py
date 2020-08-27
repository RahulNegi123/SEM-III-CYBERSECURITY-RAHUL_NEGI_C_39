def has_33(lst1):
    for i in range(len(lst1)-1): #prevent from going out of range
        if lst1[i] == 3 and lst1[i + 1] == 3:
            return True
    return False

lst = [] 
n = int(input("Enter number of elements : ")) 
print("Now, Enter the list : \n")
for i in range(0, n): 
    ele = int(input())
    lst.append(ele)
print(has_33(lst))
