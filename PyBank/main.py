import os
import csv

TotalMonths = []
Total = []
AvgChange = []
GreatestIncrease = []
GreatestDecrease = []

budget = os.path.join("Resources", "budget_data.csv")




with open(budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        # Add place
        Total.append(row[0])

        # Add population
        TotalMonths.append(row[1])

        # Average Change
        AvgChange = round(int(row[0]) / int(row[1]))

        print(AvgChange)
        
cleanedpath = list(zip(Total,TotalMonths,AvgChange))

# Set variable for output file
output_file = os.path.join('Analysis')

#  Open the output file
with open(output_file, "w", newline='') as Analysis:
    writer = csv.writer(Analysis)

    # Write the header row
    writer.writerow([Analysis])

    # Write in zipped rows
    writer.writerows(cleanedpath)
