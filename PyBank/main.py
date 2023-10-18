import os
import csv

TotalMonths = []
Total = []
AvgChange = []
GreatestIncrease = []
GreatestDecrease = []

budget_data = os.path.join("..", "Resources", "budget_data.csv")
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

