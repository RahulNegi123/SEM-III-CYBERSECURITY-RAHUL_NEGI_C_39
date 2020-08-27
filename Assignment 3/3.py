import string
def reversed_words(senCOPY):
    string = senCOPY.split()
    string.reverse()
    return ' '.join(string)
print("enter a sentence : \n")
sen=input()
print(reversed_words(sen))
