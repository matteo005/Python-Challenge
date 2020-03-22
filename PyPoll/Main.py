import os
import csv

#Create Lists needed to store values
NumVotes = []
Candidate = []
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0

#Variable to store Candidate as String


# Module for reading CSV files
csvpath = os.path.join('../..', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

        #Fill Lists with data
        NumVotes.append(int(row[0]))
        Candidate.append(row[2])

        #Update a count of each Candidate
        if row[2] == "Khan":
            KhanVotes += 1

        if row[2] == "Correy":
            CorreyVotes += 1
        
        if row[2] == "Li":
            LiVotes += 1
        
        if row[2] == "O'Tooley":
            OTooleyVotes += 1

#Count Number of Votes
TotalVotes = len(NumVotes)

#Calculate Percentage per Candidate
KhanPercentage = (KhanVotes/TotalVotes)*100
CorreyPercentage = (CorreyVotes/TotalVotes)*100
LiPercentage = (LiVotes/TotalVotes)*100
OTooleyPercentage = (OTooleyVotes/TotalVotes)*100

#Most Votes from all Candidates
MaxVote = max(KhanVotes,CorreyVotes,LiVotes,OTooleyVotes)

#Find Winner of the Election
if MaxVote == KhanVotes:
    Winner = "Khan"
elif MaxVote == CorreyVotes:
    Winner = "Correy"
elif MaxVote == LiVotes:
    Winner = "Li"
elif MaxVote == OTooleyVotes:
    Winner = "O'TooLey"

#Print all results
print("\n")
print(f"      ""Election Results")
print("---------------------------")
print(f"Total Votes:  {TotalVotes}")
print("---------------------------")
print(f"Khan: {round((KhanPercentage),3)}% ({KhanVotes})")
print(f"Correy: {round((CorreyPercentage),3)}% ({CorreyVotes})")
print(f"Li: {round((LiPercentage),3)}% ({LiVotes})")
print(f"O'Tooleys: {round((OTooleyPercentage),3)}% ({OTooleyVotes})")
print("---------------------------")
print(f"Winner: {Winner}")
print("---------------------------")


#Create PyBank.txt file
with open("PyPoll.txt", "w") as file:

    # # Write all values
    file.write("      ""Election Results")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f"Total Votes:  {TotalVotes}")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f"Khan: {round((KhanPercentage),3)}% ({KhanVotes})")
    file.write("\n")
    file.write(f"Correy: {round((CorreyPercentage),3)}% ({CorreyVotes})")
    file.write("\n")
    file.write(f"Li: {round((LiPercentage),3)}% ({LiVotes})")
    file.write("\n")
    file.write(f"O'Tooleys: {round((OTooleyPercentage),3)}% ({OTooleyVotes})")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f"Winner: {Winner}")
    file.write("\n")
    file.write("---------------------------")