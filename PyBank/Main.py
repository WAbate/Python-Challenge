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
monthtot_count = 0.0
plchange = 0.0
totalprof = 0.0
prolos_ch = []


#Open CSV & Read
with open(budget_data.csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimeter=",")
    csv_header = next(csvfile)

#count toal number of months
    for row in csv_reader:
        monthtot_count += 1
        monthtot.append(row[0])
        profloss.append(row[1])

#Total for profit and losses over entire dataset
    for number in profloss:
        totalprof = totalprof + int(number)

#Calculate the changes in "Profit/Losses" over the entire period, 
    for number in range(len(profloss)-1):
        profloss.append(int(profloss[number]-1)-int(profloss[number]))

    sum_profloss = 0
    for number in profloss:
        sum_profloss = sum_profloss + number

#then find the average of those changes
    averagechange = round(sum_profloss / (totalprof-1))


#Print
print("Financial Analysis")
print("----------------------------")
print(f"Header: {csv_header}")
print(f"Total Months: {monthtot_count}")
print(f"Total: ${totalprof}")
print(f"Average Change: ${averagechange}")
