def range_check(l,h,n):
    if n in range(l,h):
        print( " number is in the range")
    else:
        print("The number is outside the given range.")

print("Range input (will be inclusive of high and low)\n")
print("Enter low value and high value now\n")
low=int(input())
high=int(input())

print("\n now enter which number to check is in range or not\n")
num=int(input("Enter number"))

range_check(low,high+1,num)
