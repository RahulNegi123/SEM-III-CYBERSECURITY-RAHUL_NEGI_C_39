def string_count(s):
    count1=0
    count2=0
    for char in s:
        if char.isupper():
           count1=count1+1
        elif char.islower():
           count2=count2+1
        else:
           pass
    print ("No. of Upper case characters : ", count1)
    print ("No. of Lower case Characters : ", count2)


str=input("Enter string : ")
string_count(str)
