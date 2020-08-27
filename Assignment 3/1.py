def isPANGRAM(str):
   flag=1
   all_alphabets = "abcdefghijklmnopqrstuvwxyz"
   for char in all_alphabets:
      if char not in str.lower():
         flag=0
   if(flag == 1):
      print("Yes, string is a pangram")
   else:
      print("No, string is not a pangram")

sentence=input()
isPANGRAM(sentence)

