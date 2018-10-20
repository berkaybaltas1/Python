#Name: Berkay Baltas
#Date: 10/11/2018
#This program loads an image and counts the pixels that are white.


import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread(input("Enter file name " ))
countSnow = 0
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow = countSnow + 1

print("Snow count is", countSnow)
