def summer_69(list):
        sum=0
        holdPOS=0
        for i in list:
                if i==6 :                  
                        holdPOS=1
                        continue
                if i==9 and holdPOS ==1 :
                        holdPOS=False
                        continue
                if holdPOS ==0 :          
                        sum+=i
        return sum
lst = [] 
n = int(input("Enter number of elements : ")) 
print("Now, Enter the list : \n")
for i in range(0, n): 
    ele = int(input())
    lst.append(ele)
print(summer_69(lst))
