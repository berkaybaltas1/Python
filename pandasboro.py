#Name: Berkay Baltas
#Date: 10/18/18
#This program creates pandas to find NYC population

import matplotlib.pyplot as plt
import pandas as pd

pop =pd.read_csv('nycHistPop.csv' , skiprows = 5)
mess = input("Enter borough name: ")
outf = input("Enter output file name: ")
pop['Fraction'] = pop[mess]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')
fig = plt.gcf()
fig.savefig(outf)

