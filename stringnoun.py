#Name: Berkay Baltas
#Date: 10/11/2018
#This program manipulates strings

st = input("Enter nouns: ")
stcount = st.count(" ") + 1
stsplit = st.split(" ")
counter = 0
for i in stsplit:
    nouns = (i[-1])
    if nouns == "s":
        counter += 1
print("Number of words: " , stcount)
print("Fraction of your list that is plural is ", counter/stcount)


