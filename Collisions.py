#Name: Berkay Baltas
#Date: 11/1/18
#This program counts top three reasons for collisions
import pandas as pd

file = input("Enter CSV file name: ")
cols = pd.read_csv(file)
print("Top three contributing factors for collisons: ")
print(cols["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
