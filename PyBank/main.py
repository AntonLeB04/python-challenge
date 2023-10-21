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

    headline = csvfile.__next__()
    Total = 0

    for row in csvreader:
        # Sum of Total taken from Stack Overflow 'Sum a csv column in python' answered by Martijn Pieters
        Total += int((row[1]))

        # Add population
        TotalMonths = len(row[0])

        # Average Change
        #AvgChange = round(int(row[1]) / int(row[0]))

        print(TotalMonths)

cleaned_csv = list(zip(str((Total, TotalMonths))))

output_file = os.path.join("Analysis", "Financial Analysis")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Analysis for Financial Records"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
