#Name: Berkay Baltas
#Date: 10/04/18
#This program implements pseudocode for weeks and days

days = int(input("Enter number of days: " ))
weeks =days // 7
leftover = days % 7
print("Weeks: ", weeks)
print("Days: ", leftover)
