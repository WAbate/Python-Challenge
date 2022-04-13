import os
import csv

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#EXAMPLE:
# Financial Analysis
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#CSV Data Collection
budget_data = os.path.join("Resources","budget_data.csv")

#VARIABLES:
monthtot = []
profloss = []
plchange = 0.0
totalprof = 0.0
prolos_ch = []
print("Financial Analysis")
print("----------------------------")

#Open CSV & Read
with open(budget_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimeter=",")
    csv_header = next(csvfile)

#count toal number of months

