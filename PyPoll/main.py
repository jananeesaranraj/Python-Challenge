
# Import the random and csv Module
import os
import csv

#Intialising
vote_count = 0
double_count = 0
candidate= []
winner_vote = 0
winner = ""
counter= 0

# passing the file path
csvpath = os.path.join("Resources","election_data.csv")


# Reading the CSV file
with open(csvpath,'r') as votefile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(votefile,delimiter = ',')
# skip the header
    header =  next(csvreader)

# read each row of data after the header
    for row in csvreader:
        vote_count += 1
        candidate.append(row[2])

# printing to the terminal
    print("Election Results" + "\n")
    print("------------------------------------------\n")
    print("Total Votes: " + str(vote_count) + "\n")
    print("------------------------------------------\n")

# creating a dictionary for candidates and count
    candidateDict = dict()

# read each candidate
    for candi in candidate:
    # chking for the candidates name and increasing the counter
        if candi in candidateDict:
            candidateDict[candi]+=1
        else:
            candidateDict[candi]=1      

    # reaing each candidate in the dictionary
    for candi in candidateDict:
    # calculate the percenatge of votes
        percentage = round((candidateDict[candi]/vote_count) * 100 ,3)
        print(candi + ": " + str(percentage) + "% "+ " (" +str(candidateDict[candi]) + ")")
        print("\t")

    # finding the winner from the dictionary values
        if candidateDict[candi] > winner_vote:
            winner_vote = candidateDict[candi]
            winner      = candi
    
    #printing to the terminal
    print("\t")
    print("------------------------------------------\n")
    print("Winner: "+str(winner)+"\n")
    print("------------------------------------------\n")

# Specify the file to write to
output_file = os.path.join("Analysis","poll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file,"w") as text:
    
# writing to the text file
    text.write("Election Results" + "\n\n")
    text.write("------------------------------------------\n\n")
    text.write("Total Votes: " + str(vote_count) + "\n\n")
    text.write("------------------------------------------\n\n")
    for candi in candidateDict:
        percentage = round((candidateDict[candi]/vote_count) * 100 ,3)
        text.write(candi + ": " + str(percentage) + "% "+ " (" +str(candidateDict[candi]) + ")\n\n")
    text.write("------------------------------------------\n\n")
    text.write("Winner: "+str(winner)+"\n\n")
    text.write("------------------------------------------\n")
     
