#Name: Berkay Baltas
#Date: 09/13/2018
#This program shifts letters to the left

mess = input("Enter a word: ")
enc = ""

for i in mess:
    offset = -1
    shift = (ord(i) - ord('a') + offset) % 26
    newC =chr(ord('a')+shift)
    enc = enc + newC

print(enc)
    
