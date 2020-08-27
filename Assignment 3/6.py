def blackjack(n1,n2,n3):  
    sum = n1+n2+n3
    if sum <= 21:     
        return sum
    elif sum > 21 and 11 in [n1,n2,n3] :   
        newSUM = sum-10     
        if newSUM > 21:    
            return 'BUST' 
        else:         
            return newSUM   
    else: 
        return 'BUST'

print("Enter 3 numbers : \n")
num1=int(input())
num2=int(input())
num3=int(input())
print(blackjack(num1,num2,num3))