def count_primes(num):
    count = 0
    for i in range(2,num+1):
        value=True
        for j in range(2,i):
            if(i%j == 0):
                value=False
                break
        if value:
            count += 1
    return count

print("Enter a number : \n")
num=int(input())
print(count_primes(num))

