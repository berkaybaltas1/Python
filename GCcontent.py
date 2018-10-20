#Name: Berkay Baltas
#Date: 09/20/18
#This program prints out the GC-content

mess = input("Enter a DNA string: ")
gc_content = mess.count('G')+mess.count('C')
total = len(mess)
print("Length is ", total)
print("GC-content ",(gc_content/total))
