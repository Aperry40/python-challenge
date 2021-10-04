import os
import csv
csvpath = os.path.join("..","Resources", "election_data.csv")
outputFile = os.path.join("ElectionDataAnalysis.txt")       # Output as text file



totalVotes = 0
candidates = []      #list that holds the candidate data in election
candidateVotes = {} #dictionary to hold votes each candidate receives
winningCount = 0    #variable to hold winning count
winningCandidate = "" #variable to hold the winning candidate



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader) #read header row
    firstrow = next(csvreader)
    totalVotes = totalVotes + 1
    for row in csvreader:   # for each row
       totalVotes = totalVotes + 1    # same as total += 1
       if row[2] not in candidates:   # check to see if candidate in list of candidates
           candidates.append(row[2])  # if candidate not in list, add candidate
           candidateVotes[row[2]] = 1

       else: 
            candidateVotes[row[2]] += 1  # add vote to candidate's count

#print(candidateVotes)
voteOutput = ""

for candidates in candidateVotes:   # get vote count and percentage of votes
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes))*100.00
    voteOutput += f"\t{candidates}: {votePct:.2f}% ({votes})\n"
    

    if votes > winningCount:       #compare votes to winningCount
        winningCount = votes
        winningCandidate = candidates

winningCandidateOutput = f"Winner: {winningCandidate}\n---------------------------------------"
    


    #print(votes)

    #rows will be lists
        # index 0 is Voter ID
        # index 1 is County
        # index 2 is Candidate

   
output = (
    f"\n\nElection Results\n"
    f"--------------------------------\n"
    f"\tTotal Votes: {totalVotes:,} \n"
    f"--------------------------------\n"
    f"{voteOutput}"
    f"--------------------------------\n"
    f"{winningCandidateOutput}"
)

print(output) 

with open(outputFile, "w") as textFile:   # print results and export data to text file
    textFile.write(output)                # write output to text file