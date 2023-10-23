import os
import csv

TotalMonths = []
Total = []
AvgChange = []
GreatestIncrease = ["",0]
GreatestDecrease = ["",0]

# Reading the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    headline = csvfile.__next__()
    Total = 0
    TotalMonths = 0
    PreviousProfit = 0
    change = 0
    totalchange = 0
    counter = 0

    for row in csvreader:
        # Sum of Total taken from Stack Overflow 'Sum a csv column in python' answered by Martijn Pieters
        Total += int((row[1]))

        # Total Months
        TotalMonths += 1 

        currentprofit = int((row[1]))

        if PreviousProfit != 0:
            change = currentprofit - PreviousProfit
            totalchange += change
            counter += 1

        PreviousProfit = currentprofit

        if change > GreatestIncrease[1]:
            GreatestIncrease[1] = change
            GreatestIncrease[0] = row[0]

        if change < GreatestDecrease[1]:
            GreatestDecrease[1] = change
            GreatestDecrease[0] = row[0]

output = f"""
Financial Analysis
----------------------------
Total Months: {TotalMonths}
Total: ${Total}
Average Change: ${totalchange/counter:.2f}
Greatest Increase in Profits: {GreatestIncrease[0]} (${GreatestIncrease[1]})
Greatest Decrease in Profits: {GreatestDecrease[0]} (${GreatestDecrease[1]})
"""

print(output)

output_file = os.path.join("Analysis", "Financial Analysis")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    
    datafile.write(output)