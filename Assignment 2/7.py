n=int(input("Enter the limit : \n"))
lst={}
lst[2]="Prime"
print("[", end =" ") 
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            lst[i]='Non prime'
            break
        else:
            lst[i]='prime'
print(lst, end =" ")
print("]", end =" ") 
