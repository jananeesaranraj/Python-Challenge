# Import the random and csv Module
import os
import csv

# passing the file path
budget_csv = os.path.join("Resources","budget_data.csv")

#initialising
date=[]
revenue=[]
revenue_change = []

# Read the CSv file
with open(budget_csv,'r') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# skip the header
    header=next(csvreader)
#Read each row through the csvfile data in the csvreader
    for row in csvreader:
    #appending the date and revenue to the list
        date.append(row[0])
        revenue.append (int(row[1]))

    # loop through the revenue list to find the changes
    for i in range(1,len(revenue)):
    # append the difference in revenue to the new list
        revenue_change.append(revenue[i] - (revenue[i-1]))
    # calculate the average revenue change
        avr_rev_change = round(sum(revenue_change)/len(revenue_change),2)

    # find the greatest increase and greatest decrease
        greatest_increase = max(revenue_change)
        greatest_decrease = min(revenue_change)

        increase_index = revenue_change.index (greatest_increase)
        decrease_index = revenue_change.index (greatest_decrease)

    # find the corresponding increase and decrease date using the index
        greatest_increase_date =str(date[increase_index +1])
        greatest_decrease_date = str(date[decrease_index +1])
# print the reesults to the terminal
print("Finalcial Analysis \n\t" )
print("----------------------------------------------------------------")
print("\t")
print("Total Months: " + str(len(date)))
print("\t")
print("Total: $" + str(sum(revenue)))
print("\t")
print("Average Change: $" + str(avr_rev_change))
print("\t")
print("Greatest Increase in Profits: "+ str(greatest_increase_date) + " $(" + str(greatest_increase)+ ")")
print("\t")
print("Greatest Decrease in Profits: "+ str(greatest_decrease_date) + " $("+ str(greatest_decrease)+ ")")

# specify the file to write to
output_file = os.path.join("Analysis","bank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file,'w') as text:

# write the output to the text file
    text.write("Financial Analysis" + "\n\n")
    text.write("-------------------------------------------\n\n")
    text.write("Total Months: " + str(len(date)) + "\n\n")
    text.write("Total : $"+ str(sum(revenue)) + "\n\n")
    text.write("Average Change: $" + str(avr_rev_change) + "\n\n")
    text.write("Greatest Increase in Profits: "+ str(greatest_increase_date) + " $("+str(greatest_increase) +")" + "\n\n")
    text.write("Greatest Decrease in Profits: "+ str(greatest_decrease_date) + " $("+str(greatest_decrease )+")" + "\n\n")
    


