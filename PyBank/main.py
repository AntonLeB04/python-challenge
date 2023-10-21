import os
import csv

TotalMonths = []
Total = []
AvgChange = []
GreatestIncrease = []
GreatestDecrease = []

# Reading the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")




with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    headline = csvfile.next()
    Total = 0

    for row in csvreader(csvfile):
        # Add place
        Total += int(row[1])

        # Add population
        TotalMonths.append(int(row[0]))

        # Average Change
        AvgChange = round(int(row[1]) / int(row[0]))

        print(Total)
    
output_file = os.path.join("Analysis", "Financial Analysis")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Analysis for Financial Records"])

    # Write in zipped rows
    writer.writerows(Total)
