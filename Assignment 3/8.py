def spy_game(num):
        count=0
        for i in num:
                if i==0:
                        count+=1
                else:
                        pass
                if i==7:
                        count+=1
                        break
        return count==3

lst = [] 
n = int(input("Enter number of elements : ")) 
print("Now, Enter the list : \n")

for i in range(0, n): 
    ele = int(input())
    lst.append(ele)

print(spy_game(lst))

