#Name: Berkay Baltas
#Date: 09/27/18
#This creates a pyramid of pseudocode

s = input("Enter string: ")
ls = len(s)
for i in range(0,ls-1):
    print (s[0:i])
for i in range(0,ls):
    print(s[i:ls])
        
