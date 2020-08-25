def palindrome(s):
    rev=""
    for char in s:
        rev=char+rev
    if s==rev:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

str=input("Enter string to check for Palindrome\n")
palindrome(str)


