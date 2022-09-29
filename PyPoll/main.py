import os
import csv

vote_count = 0
double_count = 0
candidate= []
winner_vote = 0
Winner = ""

counter= 0

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath,'r') as votefile:
    csvreader = csv.reader(votefile,delimiter = ',')
# skip the header
    next(csvreader)

# read each row of data after the header
    for row in csvreader:
        vote_count += 1
        candidate.append(row[2])

    print("Election Results" + "\n")
    print("------------------------------------------\n")
    print("Total Votes:" + str(vote_count) + "\n")
    print("------------------------------------------\n")

    candidateDict = dict()
    for candi in candidate:
        if candi in candidateDict:
            candidateDict[candi]+=1
        else:
            candidateDict[candi]=1      

    for candi in candidateDict:
        percentage = round((candidateDict[candi]/vote_count) * 100 ,3)
        print(candi + ":" + str(percentage) + "% "+ " (" +str(candidateDict[candi]) + ")")

        if candidateDict[candi] > winner_vote:
            winner_vote = candidateDict[candi]
            winner      = candi
    print("\t")
    print("------------------------------------------\n")
    print("Winner :"+str(winner)+"\n")
    print("------------------------------------------\n")

output_file = os.path.join("Analysis","poll.txt")

with open(output_file,"w") as text:
    text.write("Election Results" + "\n")
    text.write("------------------------------------------\n")
    text.write("Total Votes:" + str(vote_count) + "\n")
    text.write("------------------------------------------\n")
    for candi in candidateDict:
        percentage = round((candidateDict[candi]/vote_count) * 100 ,3)
        text.write(candi + ":" + str(percentage) + "% "+ " (" +str(candidateDict[candi]) + ")\n")
    text.write("------------------------------------------\n")
    text.write("Winner :"+str(winner)+"\n")
    text.write("------------------------------------------\n")
     
