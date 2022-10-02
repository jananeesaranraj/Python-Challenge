# Python-Challenge
**Background**:
It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

**PyBank Challenge**:
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:
•	The total number of months included in the dataset
•	The net total amount of "Profit/Losses" over the entire period
•	The changes in "Profit/Losses" over the entire period, and then the average of those changes
•	The greatest increase in profits (date and amount) over the entire period
•	The greatest decrease in profits (date and amount) over the entire period

**Solution**:
**Steps taken to solve the challenge**:
1.	Import the random and csv Module
2.	passing the file path
3.	Initialize variables
4.	Read the CSV file
5.	CSV reader specifies delimiter and variable that holds contents
6.	Skip the header
7.	Read each row through the csvfile data in the csvreader
8.	Append the date and revenue to the list
9.	Loop through the revenue list to find the changes
10.	Append the difference in revenue to the new list
11.	Calculate the average revenue change
12.	Find the greatest increase and greatest decrease
13.	Find the corresponding increase and decrease date using the index
14.	Print the results to the terminal
15.	Specify the file to write to
16.	Open the file using "write" mode. Specify the variable to hold the contents
17.	Write the output to the text file
    
**PyPoll Challenge**:
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
•	The total number of votes cast
•	A complete list of candidates who received votes
•	The percentage of votes each candidate won
•	The total number of votes each candidate won
•	The winner of the election based on popular vote

**Solution**:
**Steps taken to solve the challenge**:
1.	Import the random and csv Module
2.	Initialize variables
3.	Passing the file path
4.	Reading the CSV file
5.	CSV reader specifies delimiter and variable that holds contents
6.	Skip the header
7.	Read each row of data after the header
8.	Print the results to the terminal
9.	Create a dictionary for candidates and count
10.	Read each candidate
11.	Check for the candidate name and increase the counter
12.	Read each candidate in the dictionary
13.	Calculate the percentage of votes
14.	Find the winner from the dictionary values
15.	Print the winner to the terminal
16.	Specify the file to write to
17.	Open the file using "write" mode. Specify the variable to hold the contents 
18.	Write the results to the text file
    
