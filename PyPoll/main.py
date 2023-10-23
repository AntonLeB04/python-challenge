import os
import csv

TotalVotes = []
StockhamVotes = []
DeGetteVotes = []
DoaneVotes = []
winner = []

# Reading the csv file
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping the header
    headline = csvfile.__next__()
    
    TotalVotes = 0
    StockhamVotes = 0
    DeGetteVotes = 0
    DoaneVotes = 0
    winner = 0

    for row in csvreader:
        
        # Total Votes
        TotalVotes += 1 
        #Votes for Stockham 
        if row[2] == "Charles Casper Stockham":
            StockhamVotes += 1
        #Votes for Degette
        if row[2] == "Diana DeGette":
            DeGetteVotes += 1
        #Votes for Doane
        if row[2] == "Raymon Anthony Doane":
            DoaneVotes += 1
        #Checking to see who is the winner
        if StockhamVotes > DeGetteVotes and DoaneVotes:
            winner = "Charles Casper Stockham"
        elif DeGetteVotes > StockhamVotes and DoaneVotes:
            winner = "Diana DeGette"
        else:
            winner = "Raymon Anthony Doane"

#Making the output file for election analysis
output = f"""
Election Results
----------------------------
Total Votes: {TotalVotes}
----------------------------
Charles Casper Stockham: {((StockhamVotes/TotalVotes)*100):.3f}% ({StockhamVotes})
Diana DeGette: {((DeGetteVotes/TotalVotes)*100):.3f}% ({DeGetteVotes})
Raymon Anthony Doane: {((DoaneVotes/TotalVotes)*100):.3f}% ({DoaneVotes})
----------------------------
Winner: {winner}
----------------------------
"""
#printing output in the terminal
print(output)
#Navigating to the Election Analysis folder
output_file = os.path.join("Analysis", "Election Analysis")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    #Printing the output
    datafile.write(str(output))