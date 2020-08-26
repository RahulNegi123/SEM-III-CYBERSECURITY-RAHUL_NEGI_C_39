def calc(i1,j2):
    res=fact(i1)//(fact(i1-j2)*fact(j2))
    return res
def fact(num):
    number=num+1
    forCALC=1
    for i in range(2,number):
        forCALC=forCALC*i
    return forCALC
rows=int(input("Enter number of rows : \n"))
for i in range(0,rows):
    for j in range(0,i+1):
        print(calc(i,j)," ",end=" ")
    print()
